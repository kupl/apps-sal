import sys
sys.setrecursionlimit(2147483647)
input=sys.stdin.readline

def search(nodes, searched, labels, v):
  searched[v] = 1
  label = labels[v]
  for l in nodes[v]:
    x, w = l
    if not searched[x]:
      if w %2 == 0:
        labels[x] = label
      else:
        labels[x] = (label + 1) % 2
      search(nodes, searched, labels, x)

def solve(n, nodes):
  searched = [0]*n
  labels = [None]*n
  labels[0] = 0
  search(nodes, searched, labels, 0)
  return labels

def main():
  n = int(input())
  nodes = [[] for _ in range(n)]
  for _ in range(n-1):
    v, u, w = map(int, input().split(' '))
    nodes[v-1].append((u-1,w))
    nodes[u-1].append((v-1,w))
  ans = solve(n, nodes)
  for r in ans:
    print(r)
  

def __starting_point():
  main()
__starting_point()

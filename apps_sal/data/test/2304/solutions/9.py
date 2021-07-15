import sys
from collections import deque
input = sys.stdin.readline

def main():
  n, m = map(int, input().split())
  tree = [[] for _ in range(n)]
  for i in range(m):
    l, r, d = map(int, input().split())
    tree[l-1].append((r-1, d))
    tree[r-1].append((l-1, -d))
  
  ans = [0]*n
  not_yet = deque([])
  already = [False]*n
  judge = True
  
  for i in range(n):
    if already[i]:
      continue
    already[i] = True
    for v in tree[i]:
      index, dist = v[0], v[1]
      ans[index] = dist
      already[index] = True
      not_yet.append(index)
    while not_yet:
      index = not_yet.popleft()
      for v in tree[index]:
        index2, dist = v[0], v[1]
        if already[index2]:
          if ans[index] + dist != ans[index2]:
            judge = False
        else:
          already[index2] = True
          ans[index2] = ans[index] + dist
          not_yet.append(index2)
          
  print("Yes" if judge else "No")
  
def __starting_point():
  main()
__starting_point()

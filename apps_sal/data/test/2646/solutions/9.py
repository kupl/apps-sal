import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,m = LI()
    route = [None] + [[] for _ in range(n)]
    for _ in range(m):
        a,b = LI()
        route[a].append(b)
        route[b].append(a)

    explored = {1}
    queue = collections.deque([1])
    ans = [None for _ in range(n+1)]
    while len(queue)!=0:
        nxt = queue.popleft()
        for nbh in route[nxt]:
            if nbh not in explored:
                ans[nbh] = nxt
                queue.append(nbh)
                explored.add(nbh)
    print("Yes")
    print(*ans[2:],sep="\n")
        
main()            


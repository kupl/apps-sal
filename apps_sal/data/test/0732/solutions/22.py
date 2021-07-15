#d=sorted(d,key=lambda x:(len(d[x]),-x))  d=dictionary     d={x:set() for x in arr}
#n=int(input())
#n,m,k= map(int, input().split())
import heapq
#for _ in range(int(input())):
#n,k=map(int, input().split())
#input=sys.stdin.buffer.readline
#for _ in range(int(input())):
def dfs(x):
    if 0< x <=n :
        s.add(x)
        x*=10
        dfs(x+i)
        dfs(x+j)

n=int(input())
#arr = list(map(int, input().split()))
s=set()

for i in range(1,10):
    for j in range(10):
        dfs(i)
print(len(s))


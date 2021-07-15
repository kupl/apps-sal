'''t=int(input())
while(t):
    t-=1
    n,k=[int(x) for x in input().split()]
    s=""
    while(len(s)!=n):
        i=0
        while(i<k):
            if len(s)==n:
                break
            s+=chr(97+i)
            i+=1
    print(s)'''

'''n=int(input())
arr=[int(x) for x in input().split()]
arr=sorted(arr)
ans=0
for i in range(0,n-1,2):
    ans+=abs(arr[i]-arr[i+1])

print(ans)'''
from collections import defaultdict
import sys,threading

def work():
    sys.setrecursionlimit(1 << 18)
    def fun(u,level,p):
        l[1]+=level*arr[u-1]
        summ[u]=arr[u-1]
        for i in graph[u]:
            if i!=p:
                fun(i,level+1,u)
                summ[u]+=summ[i]
    def fun2(u,p):
        for i in graph[u]:
            if i!=p:
                l[i]=l[u]+s-2*summ[i]
                fun2(i,u)
    n=int(input())
    n1=n
    arr=[int(x) for x in input().split()]
    graph=defaultdict(list)
    while(n1-1):
        n1-=1
        u,v=[int(x) for x in input().split()]
        graph[u].append(v)
        graph[v].append(u)
    s=0
    for i in arr:
        s+=i
    summ=[0]*(n+1)
    l=[0]*(n+1)
    fun(1,0,0)
    fun2(1,0)
    print(max(l))
def __starting_point():
    sys.setrecursionlimit(200050)
    threading.stack_size(80000000)
    thread = threading.Thread(target=work)
    thread.start()

__starting_point()

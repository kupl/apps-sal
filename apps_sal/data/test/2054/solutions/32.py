import sys
def input():return sys.stdin.readline()[:-1]
def N(): return int(input())
def NM():return list(map(int,input().split()))
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
t=N()
def f():
    a,b=NM()
    if a<b:
        a,b=b,a
    if a-b>=b:
        print(b)
    else:
        print((a+b)//3)

for i in range(t):
    f()


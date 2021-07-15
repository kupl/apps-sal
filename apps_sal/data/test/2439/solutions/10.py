from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        if sum(a) == 0:
            print("NO")
        elif sum(a) > 0:
            a.sort(reverse=True)
            print("YES")
            print(*a)
        else:
            a.sort()
            print("YES")
            print(*a)
        

def B():
    t=int(input())
    for _ in range(t):
        print(t)

def C():
    t=int(input())
    for _ in range(t):
        print(t)

def D():
    t=int(input())
    for _ in range(t):
        print(t)

A()


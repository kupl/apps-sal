t=int(input())

for i in range(t):
    L, u, l, r = map(int,input().split())
    d=0
    print(L//u - (r//u-(l-1)//u))

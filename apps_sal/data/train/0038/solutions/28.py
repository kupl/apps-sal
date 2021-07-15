t=int(input())
for i in range(t):
    n, k1, k2=list(map(int, input().split()))
    d=max(list(map(int, input().split())))
    d1=max(list(map(int, input().split())))
    if d>d1:
        print("YES")
    else:
        print("NO")


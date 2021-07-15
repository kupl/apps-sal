def solve():
    n,a,b = list(map(int,input().split()))
    worst = a+b-1
    if a+b>=n+1:
        worst = n
    best = min(n,a+b-n+1)
    if a+b<=n:
        best = 1
    print(best,worst)
t = int(input())
for _ in range(t):
    solve()


T = int(input())
for _ in range(T):
    x, y, n = list(map(int, input().split()))
    ans = (n // x)*x + y
    while(ans > n):
        ans -= x
    print(ans)


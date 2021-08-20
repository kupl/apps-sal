t = int(input())
for i in range(t):
    (n, r) = list(map(int, input().split()))
    if r >= n:
        ans = (n - 1) * n // 2 + 1
        print(ans)
    else:
        ans = r * (r + 1) // 2
        print(ans)

N = int(input())
s = list(map(int, input().split()))
ans = 0
for c in range(1, N):
    res = 0
    for k in range(1, (N - 1) // c + 1):
        a = N - 1 - c * k
        b = a - c
        res += s[c * k] + s[-c * k - 1]
        if b < 0 or (a % c == 0 and a // c <= k):
            continue
        ans = max(ans, res)
print(ans)

n, k = list(map(int, input().split()))
hs = [int(input()) for _ in range(n)]
hs.sort()
an = hs[k - 1] - hs[0]
for i in range(1, n - k + 1):
    ans = hs[i + k - 1] - hs[i]
    an = min(an, ans)
print(an)

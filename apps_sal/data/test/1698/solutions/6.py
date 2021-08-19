(n, k) = map(int, input().split())
f = list(map(int, input().split()))
f.sort(reverse=True)
ans = 0
i = 0
while i < n:
    ans += (max(f[i:i + k]) - 1) * 2
    i += k
print(ans)

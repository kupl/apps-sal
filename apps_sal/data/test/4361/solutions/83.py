n, k = map(int, input().split())
s = []
for i in range(n):
    s.append(int(input()))
s.sort()
s.reverse()
ans = s[0] - s[-1]
for i in range(n - k + 1):
    ans = min(ans, s[i] - s[i + k - 1])
print(ans)

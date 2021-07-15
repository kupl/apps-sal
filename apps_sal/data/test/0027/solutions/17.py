n = int(input())
s = str(input())
ans = len(s)
for i in range(1, n+1):
    if s[:i] + s[:i] == s[:2*i] and 2*i <= n:
        ans = min(ans, n-i+1)
print(ans)


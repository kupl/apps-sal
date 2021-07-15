n = int(input())
s = input()
ans = n
for i in range(n):
    ss = s[:i]
    if 2*i <= n and s[:i] == s[i:2*i]:
        ans = min(ans, n - i +1)
print(ans)

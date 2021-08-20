(n, k) = list(map(int, input().split()))
s = str(input())
ans = 0
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        ans += 1
if n - 1 >= ans + 2 * k:
    ans += 2 * k
else:
    ans = n - 1
print(ans)

n, k = map(int, input().split())
s = input()
x = n
for i in range(1, n):

    if s[:n - i] == s[i:]:
        x = i
        break
ans = s
for i in range(k - 1):
    ans += s[n - x:]
print(ans)

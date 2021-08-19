n = int(input())
s = input()

ans = n
for i in range(n // 2 + 1):
    if s[:i] == s[i:2 * i]:
        # print (s[:i])
        ans = min(ans, i + 1 + n - 2 * i)
print(ans)

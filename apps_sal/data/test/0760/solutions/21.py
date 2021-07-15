s = input()
k = int(input())
n = len(s)
ans = min(2 * k, 2 * n)
start = min(k + 1, n + 1)
end = (n + k) // 2 + 1
for i in range(start, end):
    flag = True
    for j in range(n - 1, max(-1, n - (i - k) - 1), -1):
        if s[j] != s[j - i]:
            flag = False
            break
    if flag:
        ans = 2 * i
for l in range(n):
    for d in range(n - l):
        if l + 2 * d <= n and s[l:l + d] == s[l + d:l + 2 * d]:
            ans = max(ans, d * 2)
print(ans)


n, p = map(int, input().split())
ans = -1
m = 1
if p == 0:
    s = bin(n)[2:]
    for i in range(len(s)):
        if s[i] == '1':
            ans += 1
    ans += 1
while n - m * p > 0 and p != 0:
    k = n - m * p
    left, right = 0, 0
    s = bin(k)[2:]
    for i in range(len(s)):
        if s[i] == '1':
            left += 1
            right += 1
        if i > 0 and s[i - 1] == '1' and s[i] == '0':
            s = s[:i] + '1' + s[i + 1:]
            right += 1
    if left <= m <= right:
        ans = m
        break
    m += 1
print(ans)

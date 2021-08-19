s = input()
k = int(input())
s = s + '?' * k
for i in range(len(s) // 2 + 1):
    a = [0] * len(s)
    for j in range(len(s) - i):
        if s[j] == s[j + i] or s[j + i] == '?':
            a[j] = 1
    c = 0
    mx = 0
    for j in a:
        if j == 1:
            c += 1
        else:
            mx = max(mx, c)
            c = 0
    if mx >= i:
        ans = i * 2
print(ans)

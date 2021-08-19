s = input()
n = len(s)
ans = 0
for i in range(2 ** (n - 1)):
    x = [0] * (n - 1)
    k = i
    for j in range(n - 1):
        x[j] += k // 2 ** (n - 2 - j)
        k -= 2 ** (n - 2 - j) * (k // 2 ** (n - 2 - j))
    a = s[0]
    for j in range(n - 1):
        if x[j] == 0:
            a = a + s[j + 1]
        else:
            ans += int(a)
            a = s[j + 1]
    ans += int(a)
print(ans)

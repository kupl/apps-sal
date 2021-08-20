s = input()
n = len(s) - 1
ans = 0
for i in range(2 ** n):
    first = ''
    for j in range(n):
        if i >> j & 1:
            ans += int(first + s[j])
            first = ''
        else:
            first += s[j]
    ans += int(first + s[-1])
print(ans)

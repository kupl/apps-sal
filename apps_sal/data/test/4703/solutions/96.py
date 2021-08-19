s = input()
ans = 0
for i in range(2 ** (len(s) - 1)):
    num = s[0]
    for j in range(len(s) - 1):
        if i >> j & 1:
            ans += int(num)
            num = ''
        num += s[j + 1]
    if len(num) != 0:
        ans += int(num)
print(ans)

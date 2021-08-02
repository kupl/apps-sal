s = input()
ans = ''
for i in range(1 << (len(s) - 1)):
    ans += s[0]
    for j in range(len(s) - 1):
        if i >> j & 1:
            ans += ' '
        ans += s[j + 1]
    ans += ' '
print(sum(map(int, ans.split())))

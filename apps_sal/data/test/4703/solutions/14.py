import copy
s = list(input())
a = []
for i in range(len(s)):
    a.append(s[i])
    if i != len(s) - 1:
        a.append('')
ans = 0
for i in range(2 ** (len(s) - 1)):
    l = copy.deepcopy(a)
    for j in range(len(s) - 1):
        if i >> j & 1:
            l[2 * j + 1] = '+'
    ans += eval(''.join(l))
print(ans)

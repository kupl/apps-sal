s = input()
l = len(s)
ans = 0
for i in range(2 ** (l-1)):
    tmp = ''
    sum = 0
    for j in range(l-1):
        tmp += s[j]
        if i >> j & 1:
            sum += int(tmp)
            tmp = ''
    sum += int(tmp + s[-1])

    ans += sum
print(ans)

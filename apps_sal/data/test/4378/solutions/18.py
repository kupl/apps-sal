n = int(input())
s = list(input()) + ['*']
a = ['*']
l = list('GRB')
c = 0
for i in range(n):
    if s[i] == a[-1]:
        for j in l:
            if j != a[-1] and j != s[i + 1]:
                a.append(j)
                c += 1
                break
    else:
        a.append(s[i])
print(c)
print(''.join(a[1:]))

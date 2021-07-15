s = input()
d = dict()
ans = '-1 -1'
for i in range(len(s)):
    if d.get(s[i]) is None:
        d[s[i]] = i
    else:
        if i - d[s[i]] <= 2:
            ans = '{a} {b}'.format(b=i + 1, a=d[s[i]] + 1)
            break
        else:
            d[s[i]] = i
print(ans)


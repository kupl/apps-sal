s = input()
n = len(s)
ans = 0
for i in range(2**(n - 1)):
    t = []
    x = i
    for j in range(n - 1):
        t.append(s[j])
        if x % 2 != 0:
            t.append('+')
        x = x // 2
    t.append(s[-1])
    m = 0
    for i in t:
        if i != '+':
            m *= 10
            m += int(i)
        else:
            ans += m
            m = 0
    ans += m
print(ans)

n = int(input())
s = input()
s = list(s)

x = []

for i in range(n):
    a = s[:i]
    b = s[i:]
    cnt = 0
    c = set(a)
    d = set(b)
    c = list(c)
    d = list(d)
    for j in range(len(c)):
        for k in range(len(d)):
            if c[j] == d[k]:
                cnt += 1
                break
    x.append(cnt)

print(max(x))

n = int(input())
s = input()
t = input()

ab = 0
abs_ = set()
ba = 0
bas = set()

for i in range(n):
    ss = s[i]
    tt = t[i]
    if ss != tt:
        if ss == 'a':
            ab += 1
            abs_.add(i+1)
        else:
            ba += 1
            bas.add(i+1)

if (ab + ba)%2 != 0:
    print(-1)
    return

res = []
if len(abs_)%2 == 1:
    first = abs_.pop()
    second = bas.pop()
    res.append((first, first))
    res.append((first, second))

while abs_:
    first = abs_.pop()
    second = abs_.pop()
    res.append((first, second))

while bas:
    first = bas.pop()
    second = bas.pop()
    res.append((first, second))

print(len(res))
for x, y in res:
    print(x, y)

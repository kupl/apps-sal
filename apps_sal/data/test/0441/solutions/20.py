(a, b, c) = list(map(int, input().split()))
b2 = b
c2 = c
d2 = input()
d = []
for i in range(len(d2)):
    d.append(d2[i])
k = 0
for i in range(len(d)):
    if d[i] == '.':
        if i > 0:
            if d[i - 1] == '*':
                if b < c:
                    d[i] = 2
                    c -= 1
                else:
                    d[i] = 1
                    b -= 1
            elif d[i - 1] == 1:
                d[i] = 2
                c -= 1
            else:
                d[i] = 1
                b -= 1
        elif b < c:
            d[i] = 2
            c -= 1
        else:
            d[i] = 1
            b -= 1
res = 0
if b >= 0:
    res += b2 - b
else:
    res += b2
if c >= 0:
    res += c2 - c
else:
    res += c2
print(res)

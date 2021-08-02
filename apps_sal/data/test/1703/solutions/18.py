n = int(input())
openw = [0 for i in range(300001)]
closew = [0 for j in range(300001)]
reg = 0
for i in range(n):
    r = input()
    c = 0
    o = 0
    e = 1
    for y in r:
        if y == ")":
            c = c + 1
        else:
            o = o + 1
        if c > o:
            e = 2
    r1 = r[::-1]
    c1 = 0
    o1 = 0
    e1 = 0
    for u in r1:
        if u == ")":
            c1 = c1 + 1
        else:
            o1 = o1 + 1
        if (o1 > c1):
            e1 = 1
    if (o == c and e == 1):
        reg = reg + 1
    elif (o > c and e == 1):
        openw[o - c] = openw[o - c] + 1
    elif (o < c and e1 == 0):
        closew[c - o] = closew[c - o] + 1
    else:
        continue
ans = 0
for j in range(0, 300001):
    ans = ans + closew[j] * openw[j]
ans = ans + reg**2
print(ans)

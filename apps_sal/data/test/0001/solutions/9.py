x = input()
l = len(x)
x = int(x)
s = '9' * l
sx = str(x)
m = int(s)
c = 0
while c != 1:
    if m > x:
        m = m - 10 ** (l - 1)
    else:
        c = 1
sm = str(m)
mm = []
for i in range(len(sm)):
    mm.append(int(sm[i]))
xx = []
for i in range(l):
    xx.append(int(sx[i]))
if m == x:
    print(m)
elif sum(xx) == sum(mm):
    print(x)
else:
    k = len(xx) - 1
    while k >= 0:
        if sum(xx) < sum(mm):
            if xx[k] == 9:
                k -= 1
            else:
                xx[k] = 9
                xx[k - 1] -= 1
                k -= 1
        else:
            if xx[0] == 0:
                xx.remove(0)
            for b in range(len(xx)):
                xx[b] = str(xx[b])
            ww = ''.join(xx)
            print(ww)
            break

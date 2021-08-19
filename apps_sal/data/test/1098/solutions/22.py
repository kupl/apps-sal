def dist(a, b):
    minsa = int(a.split(':')[0]) * 60 + int(a.split(':')[1])
    minsb = int(b.split(':')[0]) * 60 + int(b.split(':')[1])
    return minsb - minsa - 1


def ldist(a, b):
    minsa = (int(a.split(':')[0]) + 24) * 60 + int(a.split(':')[1])
    minsb = int(b.split(':')[0]) * 60 + int(b.split(':')[1])
    return minsa - minsb - 1


a = int(input())
x = []
for i in range(a):
    t = input()
    x.append(t)
x = sorted(x)
ans = 0
for i in range(0, len(x) - 1):
    r = dist(x[i], x[i + 1])
    ans = max(r, ans)
ans = max(ans, ldist(x[0], x[len(x) - 1]))
h = ans // 60
m = ans - h * 60
if h < 10:
    if m < 10:
        print('0' + str(h) + ':0' + str(m))
    else:
        print('0' + str(h) + ':' + str(m))
elif m < 10:
    print(str(h) + ':0' + str(m))
else:
    print(str(h) + ':' + str(m))

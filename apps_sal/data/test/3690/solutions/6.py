3


def dstr(a, b):
    return (b - a) % (12 * 60 * 60)


h, m, s, t1, t2 = list(map(int, input().split()))

cd = [(h * 60 * 60 + m * 60 + s) % (12 * 60 * 60), m * 12 * 60 + s, s * 12 * 60]
if dstr(cd[0], cd[2]) < dstr(cd[0], cd[1]):
    cd = cd[::-1]

t1 *= 60 * 60
t2 *= 60 * 60


ans = False

for i in range(-1, 2):
    if dstr(cd[i], t1) <= dstr(cd[i], cd[i + 1]) \
       and dstr(cd[i], t2) <= dstr(cd[i], cd[i + 1]):
        ans = True

if len(set(cd)) == 1:
    ans = True

if ans:
    print("YES")
else:
    print("NO")

import bisect
d = [1]
p = [1]
LIM = 10**9 + 2
last_dig = [1]


def get(x):
    n = x - 1
    x, y = 1, 9
    while n > x * y:
        n, x, y = n - x * y, x + 1, y * 10
    a = str(10 ** (x - 1) + n // x)[n % x]
    print(a)


while True:
    last_dig.append(last_dig[-1] + 1)
    d.append(d[-1] + len(str(last_dig[-1])))
    p.append(p[-1] + d[-1])
    if p[-1] > LIM:
        break

q = int(input())
for i in range(q):
    quer = int(input())
    if(quer == 1):
        print("1")
        continue
    gg = bisect.bisect_right(p, quer) - 1
    rem = quer - p[gg]
    if(rem == 0):
        rem = d[gg]
    get(rem)

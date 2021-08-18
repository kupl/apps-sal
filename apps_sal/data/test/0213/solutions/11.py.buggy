n, m = list(map(int, input().split()))
data = []
fl = [0] * 1000000
an = -1
f = 0
for i in range(m):
    data += [list(map(int, input().split()))]
    fl[data[i][0]] = data[i][1]
    if data[i][0] == n:
        an = data[i][1]
    f = max(data[i][1], f)


if an != -1:
    print(an)
    return
data.sort()

an = []
t = True
for i in range(m):
    if data[i][0] != data[i][1]:
        t = False
if t:
    an += [n]

for k in range(2, 10001):
    # print(k)
    t = True
    for i in range(m):
        f = data[i][0] // k + min(1, data[i][0] % k)
        if data[i][1] != f:
            t = False
            break
    if not t:
        continue

    an += [n // k + min(1, n % k)]
    # print(an)

if len(set(an)) == 1:
    print(an[0])
else:
    print(-1)

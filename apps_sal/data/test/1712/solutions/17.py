(n, x, y) = list(map(int, input().split()))
a = list()
for i in range(n):
    a.append(int(input()))
hits = 0
cx = 1
cy = 1
r = list()
while hits < x + y:
    if cx / x < cy / y:
        cx += 1
        hits += 1
        r.append('Vanya')
    elif cx / x > cy / y:
        cy += 1
        hits += 1
        r.append('Vova')
    else:
        cy += 1
        cx += 1
        hits += 2
        r.append('Both')
        r.append('Both')
for m in a:
    print(r[(m - 1) % (x + y)])

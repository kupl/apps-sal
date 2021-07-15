p, y = list(map(int, input().split()))

mx = 33000

v = [False]*mx
for x in range(2, mx):
    if not v[x]:
        for i in range(x*x, mx, x):
            v[i] = True
primes = [i for i, _ in enumerate(v) if not _ and i>1]
fail = True
for v in range(y, p, -1):
    fail = False
    for pr in primes:
        if pr <= p and v%pr == 0:
            fail = True
        elif pr > p: break
    if not fail:
        print(v)
        break

if fail:
    print(-1)




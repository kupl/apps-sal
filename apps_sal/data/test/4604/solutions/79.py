n = int(input())
A = tuple(map(int, input().split()))
mod = 10**9 + 7

niseven = (n % 2 == 0)

cd = dict()
for a in (A):
    cd.setdefault(a, 0)
    cd[a] += 1
    if a == 0 and cd[a] > 1:
        print((0))
        break
    if a > 0 and cd[a] > 2:
        print((0))
        break
    if (a % 2 == 0) == niseven:
        print((0))
        break
else:
    print((pow(2, n // 2, mod)))

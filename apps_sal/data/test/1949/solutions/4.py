(n, k) = list(map(int, input().split()))
a = list(map(int, set(input().split())))
a.sort()
rk = iter(list(range(k)))
prv = 0
for (x, _) in zip(a, rk):
    print(x - prv)
    prv = x
for __ in rk:
    print('0')

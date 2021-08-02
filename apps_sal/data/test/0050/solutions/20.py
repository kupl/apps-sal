n, m, r = map(int, input().split())

s = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

mi = min(s)
ma = max(b)

if mi < ma:
    print((r // mi) * ma + r % mi)
else:
    print(r)

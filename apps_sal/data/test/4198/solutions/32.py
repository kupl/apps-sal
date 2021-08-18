a, b, x = map(int, input().split())

ok = 0
ng = pow(10, 9) + 1

while abs(ng - ok) > 1:
    mid = int((ok + ng) / 2)
    c = a * mid + b * len(str(mid))
    if c <= x:
        ok = mid
    else:
        ng = mid

print(ok)

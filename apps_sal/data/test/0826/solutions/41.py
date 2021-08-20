N = int(input())
ok = 0
ng = 10 ** 18 + 1
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if N + 1 >= mid * (mid + 1) // 2:
        ok = mid
    else:
        ng = mid
print(N - ok + 1)

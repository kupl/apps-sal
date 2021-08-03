n, k = map(int, input().split())
a = list(map(int, input().split()))
ng = 0
ok = 10**10
while ok - ng > 1:
    m = (ok + ng) // 2
    c = 0
    for i in a:
        c += (i // m - (i % m == 0))
    if c <= k:
        ok = m
    else:
        ng = m
print(ok)

n = int(input())
ok = 10 ** 20
ng = 0
while ok - ng > 1:
    m = (ok + ng) // 2
    if m * (m + 1) <= 2 * (n + 1):
        ng = m
    else:
        ok = m
print(n + 1 - ng)

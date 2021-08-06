n = int(input())


def is_ok(x):
    if (n - x + 1) * (n - x + 2) // 2 <= n + 1:
        return True
    else:
        return False


ng = 0
ok = n
while ng + 1 < ok:
    c = (ok + ng) // 2
    if is_ok(c):
        ok = c
    else:
        ng = c
print(ok)

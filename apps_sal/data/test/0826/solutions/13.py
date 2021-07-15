n = int(input())
ok, ng = 0, 10 ** 18
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    m = (mid * (mid + 1)) // 2
    if m <= n + 1:
        ok = mid
    else:
        ng = mid

# n+1をバラせば1~okまでカバーできる
print((n - ok + 1))



(n, a, b) = list(map(int, input().split()))
h = [int(input()) for i in range(n)]
ng = 0
ok = 10 ** 9
while ok - ng > 1:
    mid = (ok + ng) // 2
    s = 0
    for i in h:
        s += max(0, (i - mid * b + a - b - 1) // (a - b))
    if s <= mid:
        ok = mid
    else:
        ng = mid
print(ok)


n, a, b = list(map(int, input().split()))
hitpoints = [int(input()) for _ in range(n)]

additional = a - b


def feasible(k):
    additional_num = sum([max((hp - (b * k) + additional - 1) // additional, 0) for hp in hitpoints])
    return additional_num <= k


ok = 10**9 + 1
ng = 0

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if feasible(mid):
        ok = mid
    else:
        ng = mid

print(ok)

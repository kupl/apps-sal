n, h = list(map(int, input().split()))
a = list(map(int, input().split()))


def can(mid):
    val = sum(sorted(a[:mid])[::-2])
    return val <= h


le = 1
rg = n + 1

while rg - le > 1:
    mid = (le + rg) // 2

    if can(mid):
        le = mid
    else:
        rg = mid

print(le)

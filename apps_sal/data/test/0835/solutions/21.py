burger = input()
b = burger.count('B')
s = burger.count('S')
c = burger.count('C')
(nb, ns, nc) = map(int, input().split())
(pb, ps, pc) = map(int, input().split())
money = int(input())


def ok(target):
    costB = max(0, (target * b - nb) * pb)
    costS = max(0, (target * s - ns) * ps)
    costC = max(0, (target * c - nc) * pc)
    return costC + costB + costS <= money


low = 0
high = int(1e+18)
while low < high:
    mid = (high + low + 1) // 2
    if ok(mid):
        low = mid
    else:
        high = mid - 1
print(high)

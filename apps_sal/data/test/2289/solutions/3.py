import bisect

N, Q = list(map(int, input().split()))
ws = list(map(int, input().split()))
qs = list(map(int, input().split()))

cums = [0]
for w in ws:
    cums.append(cums[-1] + w)

damage = 0
for q in qs:
    damage += q
    if damage >= cums[-1]:
        damage = 0
        print(N)
    else:
        i = bisect.bisect(cums, damage)
        print(N - i + 1)

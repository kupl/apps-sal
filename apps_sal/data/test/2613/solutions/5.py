t = int(input())

for _ in range(t):
    n, k, z = list(map(int, input().split()))

    a = list(map(int, input().split()))
    nei = list(a1 + a2 for a1, a2 in zip(a, a[1:]))

    best = 0
    for lefts in range(z + 1):
        rights = k - lefts
        for final_left in [False, True]:
            if rights < 1 + lefts - final_left:
                continue

            total = sum(a[:rights - lefts + final_left + 1])
            if final_left:
                total += a[rights - lefts]
            total += (lefts - final_left) * max(nei[:rights - lefts + final_left])
            best = max(best, total)
    print(best)

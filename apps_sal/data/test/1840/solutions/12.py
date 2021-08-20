import bisect


def cummulative_sum(arr):
    acc = 0
    newarr = [[0, 0]]
    for (defence, gold) in arr:
        acc += gold
        if newarr[-1][0] == defence:
            newarr[-1][1] += gold
        else:
            newarr.append([defence, acc])
    return newarr


(spaceship_count, base_count) = list(map(int, input().strip().split()))
spaceships = list(map(int, input().strip().split()))
bases = []
answer = []
for _ in range(base_count):
    (d, g) = list(map(int, input().strip().split()))
    bases.append((d, g))
bases.sort()
bases_prefixes = cummulative_sum(bases)
for spaceship in spaceships:
    i = bisect.bisect_right(bases_prefixes, [spaceship, 10 ** 15])
    answer.append(bases_prefixes[i - 1][1])
print(*answer)

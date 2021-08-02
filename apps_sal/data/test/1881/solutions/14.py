import sys

n, k = list(map(int, next(sys.stdin).rstrip().split()))

xs = list(map(int, next(sys.stdin).rstrip().split()))

mapka = {}
lengths = {}

result = []

for x in xs:

    if x in mapka:
        result.append(mapka[x])
    else:
        left = max(0, x - k + 1)
        range_potential = x - left
        for i in range(range_potential, -1, -1):
            potential_left = x - i
            if potential_left not in mapka:
                result.append(potential_left)
                for y in range(potential_left, x + 1):
                    mapka[y] = potential_left

                lengths[potential_left] = x - potential_left + 1

                break
            else:

                if lengths[mapka[potential_left]] + (x - potential_left) <= k:
                    result.append(mapka[potential_left])
                    for y in range(mapka[potential_left] + lengths[mapka[potential_left]], x + 1):
                        mapka[y] = mapka[potential_left]
                        lengths[mapka[potential_left]] += 1

                    break

print(' '.join(map(str, result)))

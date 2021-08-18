
import itertools
n, a, b, c = list(map(int, input().split()))
nums = [int(input()) for _ in range(n)]

ans = 10**10

for usage_info in itertools.product(list(range(4)), repeat=n):

    mp = 0
    length = [0, 0, 0]
    for idx, usage in enumerate(usage_info):
        if usage == 3:
            continue
        if length[usage] > 0:
            mp += 10
        length[usage] += nums[idx]
    if min(length) == 0:
        continue

    mp += abs(length[0] - a) + abs(length[1] - b) + abs(length[2] - c)
    ans = min(ans, mp)

print(ans)

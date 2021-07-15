n = int(input())
nums = list(map(int, input().strip().split(' ')))

snums = sorted(enumerate(nums), key=lambda x: x[1])

bonus = set()
holes = set()
skip = set()
count = 1

for i, v in snums:
    if v < count or v > n:
        bonus.add(i)
    if v == count:
        count += 1
    elif v > count:
        holes.update(j for j in range(min(n+1, count), min(n+1, v)))
        count = v + 1

while len(bonus) > 0 and len(holes) > 0:
    idx = bonus.pop()
    x = holes.pop()
    nums[idx] = x
    skip.add(idx)

if len(holes) == 0:
    last = snums[-1][1] + 1
    for i in bonus:
        nums[i] = last
        last += 1
else:
    assert(len(bonus) == 0)
    for i, v in snums[::-1]:
        if i in skip:
            continue
        if len(holes) == 0:
            break
        x = holes.pop()
        nums[i] = x

print(' '.join([str(x) for x in nums]))


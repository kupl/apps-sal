from collections import Counter

n = int(input().strip())
nums = list(map(int, input().strip().split()))

res = 0
state = []
counter = Counter()
prev = {
    8: 4,
    15: 8,
    16: 15,
    23: 16,
    42: 23,
}
good_nums = [4, 8, 15, 16, 23, 42]

for i, num in enumerate(nums):
    if num == 4:
        counter[num] += 1
    elif counter[num] < counter[prev[num]]:
        counter[num] += 1
        if num == 42:
            for good_num in good_nums:
                counter[good_num] -= 1
    else:
        res += 1

res += sum(counter.values())

print(res)

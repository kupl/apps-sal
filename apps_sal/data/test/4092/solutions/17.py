input()
prefix_sums = set()
prefix_sums_shift = 1000
result = 0
for x in map(int, input().split()):
    if prefix_sums_shift - x in prefix_sums:
        result += 1
        prefix_sums = set()
        prefix_sums_shift = 0
    prefix_sums_shift -= x
    prefix_sums.add(x + prefix_sums_shift)
print(result)

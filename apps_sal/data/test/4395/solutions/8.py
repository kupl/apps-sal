import itertools
n = int(input())
s = input()
best_pattern = None
best_count = None
for pattern in itertools.permutations('RGB', 3):
    count = 0
    for (i, ch) in enumerate(s):
        if ch != pattern[i % 3]:
            count += 1
    if best_count is None or best_count > count:
        (best_count, best_pattern) = (count, pattern)
print(best_count)
(full, tail) = divmod(n, 3)
print(''.join(best_pattern * full + best_pattern[:tail]))

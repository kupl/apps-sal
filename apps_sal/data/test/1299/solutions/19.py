(n, k) = [int(x) for x in input().split()]
absurd_scores = [int(x) for x in input().split()]
partial_sums = [0]
for idx in range(len(absurd_scores)):
    partial_sums.append(partial_sums[-1] + absurd_scores[idx])
a = n - 2 * k
b = n - k
max_sum = partial_sums[n] - partial_sums[n - 2 * k]
cur_top_idx = n - k
cur_top_max = partial_sums[n] - partial_sums[n - k]
for i in reversed(list(range(n - 2 * k))):
    new_top_idx = i + k
    new_top_sum = partial_sums[new_top_idx + k] - partial_sums[new_top_idx]
    if new_top_sum >= cur_top_max:
        cur_top_max = new_top_sum
        cur_top_idx = new_top_idx
    new_low_idx = i
    new_sum = partial_sums[new_low_idx + k] - partial_sums[new_low_idx] + cur_top_max
    if new_sum >= max_sum:
        a = new_low_idx
        b = cur_top_idx
        max_sum = new_sum
print(a + 1, b + 1)
"\nMust cover entire range [1 4 5 6] for len 2\nSmallest idx is 2nd largest value\nCan't be greedy taking the max one immediately [2 1 99 100 98] for len 2\n"

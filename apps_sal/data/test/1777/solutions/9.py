from collections import defaultdict


def solve():
    n = int(input())
    seqs = defaultdict(list)
    for _ in range(n):
        seq = input()
        seq = [1 if c == '(' else -1 for c in seq]
        cumm_sum = [0 for _ in range(len(seq) + 1)]
        for i in range(len(seq)):
            cumm_sum[i + 1] = seq[i] + cumm_sum[i]

        value = sum(seq)
        height = min(cumm_sum)

        if value >= 0 and height < 0:
            continue
        if value < 0 and height < value:
            continue

        seqs[value].append(height)

    num_pairs = 0
    for val in seqs:
        if val < 0: continue
        if val == 0: num_pairs += len(seqs[val]) // 2
        if val > 0 and (-val) in seqs:
            num_pairs += min(len(seqs[val]), len(seqs[-val]))

    print(num_pairs)


solve()

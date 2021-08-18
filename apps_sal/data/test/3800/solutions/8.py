from collections import Counter


def __starting_point():
    a = int(input())
    seq = list(input())
    n = len(seq)
    seq = [int(x) for x in seq]

    curr_sum = 0
    cum_sum = [0]
    sum_pairs = list()

    for i in seq:
        curr_sum += i
        cum_sum.append(curr_sum)
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i <= j:
                sum_pairs.append(cum_sum[j] - cum_sum[i - 1])

    freq = Counter(sum_pairs)

    unique_sum = list(freq.keys())
    unique_sum = set(unique_sum)
    ans = 0

    for i in unique_sum:
        if i != 0 and a % i == 0 and a // i in freq:
            if i != a // i:
                ans += (freq[i] * freq[a // i])
            else:
                ans += (freq[i] * (freq[i]))
                freq.pop(i)

    if a == 0:
        ans = (freq[0] * len(sum_pairs)) + (freq[0] * (len(sum_pairs) - freq[0]))

    print(ans)


__starting_point()

def check(lengths, k, full_count_of_opposite):
    maxcount = 0
    count = 0
    start = 0
    cur_k = k
    for (i, el) in enumerate(lengths):
        if i % 2 == 0:
            count += el
        elif cur_k - el >= 0:
            cur_k -= el
        else:
            maxcount = max(count, maxcount)
            cur_k -= el
            while start < i and cur_k < 0:
                count -= lengths[start]
                cur_k += lengths[start + 1]
                start += 2
            if start > i:
                cur_k = k
                count = 0
    maxcount = max(count, maxcount)
    result = maxcount + min(k, full_count_of_opposite)
    return result


def maxsubsl(s, k):
    lengths = []
    prev = s[0]
    cnt = 0
    full_counts = [0, 0]
    for el in s:
        if el != prev:
            lengths.append(cnt)
            cnt = 0
        prev = el
        cnt += 1
        full_counts[len(lengths) % 2] += 1
    lengths.append(cnt)
    maxl = check(lengths, k, full_counts[1])
    if len(lengths) > 1:
        maxl = max(maxl, check(lengths[1:], k, full_counts[0]))
    return maxl


(_, k) = list(map(int, input().split()))
s = input()
print(maxsubsl(s, k))

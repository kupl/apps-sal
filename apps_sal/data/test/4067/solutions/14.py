from collections import defaultdict


def solve():
    n = int(input())

    s = list(input())

    freq = defaultdict(int)

    for i in range(n):
        freq[s[i]] += 1

    zero_cnt = 0
    one_cnt = 0

    for i in range(n):
        if s[i] == "0" and zero_cnt < n // 3:
            zero_cnt += 1
            continue

        if freq["0"] < n // 3:
            if freq[s[i]] > n // 3:
                freq[s[i]] -= 1
                freq["0"] += 1
                s[i] = "0"
                continue

        if s[i] == "1" and one_cnt < n // 3:
            one_cnt += 1
            continue

        if freq["1"] < n // 3:
            if freq[s[i]] > n // 3:
                freq[s[i]] -= 1
                freq["1"] += 1
                s[i] = "1"
                continue

        if freq["2"] < n // 3:
            if freq[s[i]] > n // 3:
                freq[s[i]] -= 1
                freq["2"] += 1
                s[i] = "2"
                continue

    print(''.join(k for k in s))


solve()

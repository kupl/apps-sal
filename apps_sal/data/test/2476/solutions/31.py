from collections import Counter
import bisect


def main():
    N = int(input())
    A = list(map(int, input().split()))
    count_list = list(Counter(A).values())
    count_list.sort()
    cumsum_count = [0] * len(count_list)
    cumsum_count[0] = count_list[0]
    for i in range(1, len(count_list)):
        cumsum_count[i] = cumsum_count[i - 1] + count_list[i]
    ans_list = [0] * N
    n_max = N
    for k in range(1, len(count_list) + 1):
        n_max = min(n_max, N // k)
        s = 0
        while True:
            index = bisect.bisect_left(count_list, n_max)
            s = n_max * (len(count_list) - index)
            if index > 0:
                s += cumsum_count[index - 1]
            if s >= k * n_max or n_max == 0:
                break
            n_max -= 1
        ans_list[k - 1] = n_max
    for ans in ans_list:
        print(ans)


def __starting_point():
    main()


__starting_point()

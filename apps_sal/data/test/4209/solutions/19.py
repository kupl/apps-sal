def index(key, item, index):
    if key in index:
        index[key].append(item)
    else:
        index[key] = [item]


def schedule(times):
    index_by_b = {}
    for time in times:
        index(time[1], time, index_by_b)
    b_keys = sorted(list(index_by_b.keys()))
    result = []
    a_min = 0
    # Get interval with minimun end time whose start time >= a_min.
    for end_time in b_keys:
        start = index_by_b[end_time][-1][0]
        if start >= a_min:
            result.append((start, end_time))
            a_min = end_time
    return result


def solve(n, a_l):
    index_by_sum = {}
    for i in range(n):
        sum_ = 0
        for j in range(i + 1, n + 1):
            sum_ += a_l[j - 1]
            if sum_ in index_by_sum:
                index_by_sum[sum_].append((i, j))
            else:
                index_by_sum[sum_] = [(i, j)]
    result = []
    for sum_, times in index_by_sum.items():
        sub_result = schedule(times)
        if len(sub_result) > len(result):
            result = sub_result
    return result


def main():
    n = int(input())
    a_l = list(map(int, input().split()))
    result = solve(n, a_l)
    print(len(result))
    for a, b in result:
        print(a + 1, b)


def __starting_point():
    main()


__starting_point()

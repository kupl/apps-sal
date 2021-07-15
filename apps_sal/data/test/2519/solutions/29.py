def main():
    n, k = map(int, input().split())
    p_lst = list(map(int, input().split()))
    lst = []

    for i in range(n):
        lst.append((p_lst[i] + 1) / 2)

    tmp_sum = sum(lst[:k])
    maximum = tmp_sum
    for i in range(n - k):
        tmp_sum -= lst[i]
        tmp_sum += lst[i + k]
        maximum = max(maximum, tmp_sum)

    print(maximum)


def __starting_point():
    main()
__starting_point()

def binary_search(arr, num):
    left = 0
    right = len(arr) - 1
    while right - left > 0:
        mid = (left + right) // 2
        if arr[mid] > num:
            right = mid
        else:
            left = mid + 1
    if arr[left] > num:
        return left
    else:
        return len(arr)


def main():
    n, m, k = map(int, input().split())
    a_books = list(map(int, input().split()))
    b_books = list(map(int, input().split()))
    b_cum_sum = [0] * (m + 1)
    for i in range(m):
        b_cum_sum[i + 1] = b_cum_sum[i] + b_books[i]
    current = 0
    ans = 0
    for i in range(n + 1):
        if i > 0:
            current += a_books[i - 1]
        if current > k:
            break
        rest = k - current
        index = binary_search(b_cum_sum, rest)
        ans = max(ans, i + index - 1)
    print(ans)


def __starting_point():
    main()


__starting_point()

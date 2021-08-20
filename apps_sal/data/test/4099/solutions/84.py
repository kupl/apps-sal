(n, k, m) = map(int, input().split())
a = list(map(int, input().split()))
result = m * n - sum(a)


def show_result():
    if result > k:
        return -1
    elif 1 <= result <= k:
        return result
    elif result <= 0:
        return 0


print(show_result())

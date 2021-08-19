a = int(input())


def ans(n, p=1):
    return ans((n + 1) // 2, p * 2) + n // 2 * p if n > 1 else 0


print(ans(a))

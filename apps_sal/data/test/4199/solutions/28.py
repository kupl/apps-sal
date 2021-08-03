n, k = list(map(int, input().split()))
h = list(map(int, input().split()))


def answer(n: int, k: int, h: list) -> int:
    ans = 0
    for i in range(0, n):
        if h[i] >= k:
            ans += 1
    return ans


print((answer(n, k, h)))

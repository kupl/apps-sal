n, k = list(map(int, input().split()))
a = list(map(int, input().split()))


def card(N, K, A):
    card = sorted(A, reverse=True)
    s = 0
    ans = 0
    for i in card:
        if s + i < K:
            s += i
            ans += 1
        else:
            ans = 0
    return ans


print((card(n, k, a)))

A, B = list(map(int, input().split()))


def calc(a):
    t = (a + 1) // 2
    ans = t % 2
    if a % 2 == 0:
        ans = ans ^ a
    return ans


print((calc(A - 1) ^ calc(B)))

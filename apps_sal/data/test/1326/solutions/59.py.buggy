N = int(input())
if N == 1:
    print((1))
    return


def divisor(n):
    m = N // n
    return n * m * (m + 1) // 2


M = N // 2
ans = 0
for i in range(2, M + 1):
    ans += divisor(i)
ans += N * (N + 1) - M * (M + 1) // 2
print(ans)

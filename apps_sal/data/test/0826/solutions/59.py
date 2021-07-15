# 1...s = 1 / 2 * s(s + 1)
# n + 1 = 1 / 2 * s(s + 1)
# 2n + 2 = s(s+1)
# s = (-1 + pow(1 + 4 * (2 + 2 * n), 0.5)) / 2
# n = 10^18 -> s = 1414213561.837... < 10^10

n = int(input())
left = 0
right = 10 ** 10
while right - left > 1:
    mid = (right + left) // 2
    if mid * (mid + 1) <= 2 * n + 2:
        left = mid
    else:
        right = mid
print((n - left + 1))


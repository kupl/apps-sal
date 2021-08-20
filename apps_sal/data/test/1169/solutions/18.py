import math
(n, m) = list(map(int, input().split()))
MINANS = max(0, n - m * 2)


def combi(m):
    return m * (m - 1) // 2


for i in range(int(math.sqrt(2 * m)), n + 1):
    if combi(i) >= m:
        break
MAXANS = n - i
print(MINANS, MAXANS)

import math
t = int(input())
for i in range(t):
    n, k = list(map(int, input().split(" ")))
    k -= 1  # zero-index
    m = int((1 + math.sqrt(1 + 8 * k)) / 2)
    tri = int(m * (m - 1) / 2)
    s = k - tri
    # print(m)
    # print(s)
    s = "a" * (n - m - 1) + "b" + "a" * (m - s - 1) + "b" + "a" * s
    print(s)

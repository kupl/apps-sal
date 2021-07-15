import math
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    mx = max(x[0], n - x[-1] + 1)
    for i in range(1, k):
        mx = max(math.floor((x[i] - x[i - 1]) / 2) + 1, mx)
    print(mx)

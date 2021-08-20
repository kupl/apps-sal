(n, m, k) = list(map(int, input().split()))
ai = list(map(int, input().split()))
ar = [0] * k
for i in range(m):
    (x, y) = list(map(int, input().split()))
    x -= 1
    if x < k:
        ar[x] = max(ar[x], y)
ai.sort()
big = 10 ** 9
ar2 = [big] * (k + 1)
ar3 = [0] * (k + 1)
ar3[0] = 0
for i in range(1, k + 1):
    ar3[i] = ar3[i - 1] + ai[i - 1]
ar2[k] = 0
for i in range(k, 0, -1):
    for j in range(i):
        ar2[i - j - 1] = min(ar2[i - j - 1], ar2[i] + ar3[i] - ar3[i - (j + 1 - ar[j])])
print(ar2[0])

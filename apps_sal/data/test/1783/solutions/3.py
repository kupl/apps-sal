n, k = list(map(int, input().split()))
ai = list(map(int, input().split()))
summ = 0
k2 = n - k + 1
for i in range(n):
    summ += ai[i] * min(k2, k, i + 1, n - i)
print(summ / (k2))

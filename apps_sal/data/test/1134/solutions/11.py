n = int(input())
m = list(map(int, input().split()))
t = [1] * n
for i in range(1, n):
    t[i] = max(t[i - 1], m[i] + 1)
for i in range(n - 2, -1, -1):
    t[i] = max(t[i], t[i + 1] - 1)
summ = 0
for i in range(n):
    summ += t[i] - m[i] - 1
print(summ)

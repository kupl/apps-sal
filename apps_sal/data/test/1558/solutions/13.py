n, r, avg = map(int, input().split())
avg *= n
a = [0] * n
b = [0] * n
mas = [[0, 0]] * n
summ = 0
for i in range(n):
    a[i], b[i] = map(int, input().split())
    summ += a[i]
    mas[i] = [b[i], a[i] - r]
mas.sort()
for i in range(n):
    mas[i][1] *= -1
i = 0
cnt = 0
while i < n and summ < avg:
    cnt += min(mas[i][1], avg - summ) * mas[i][0]
    summ += min(mas[i][1], avg - summ)
    i += 1
print(cnt)

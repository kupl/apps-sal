n, b, d = map(int, input().split())
a = list(map(int, input().split()))
c = 0
summ = 0
for i in range(n):
    if a[i] <= b:
        summ += a[i]
    if summ > d:
        c += 1
        summ = 0

print(c)

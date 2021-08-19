(n, x) = map(int, input().split())
nach = 1
summa = 0
for i in range(n):
    (l, r) = map(int, input().split())
    while nach + x <= l:
        nach += x
    while nach + 1 <= r + 1:
        nach += 1
        summa += 1
print(summa)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [a[i] - b[i] for i in range(n)]
c.sort()
ind = n - 1
wyn = 0
for i in range(n):
    while True:
        if ind > i and c[i] + c[ind] > 0:
            ind -= 1
        else:
            break

    if ind <= i:
        ind = min(n - 1, i)
    wyn += (n - 1 - ind)
print(wyn)

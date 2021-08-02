n = int(input())
a = list(map(int, input().split()))
minn = 10000000
for i in range(n):
    summ = 0
    for j in range(n):
        summ += a[j] * 2 * (abs(j) + abs(j - i) + abs(i))
    if summ < minn:
        minn = summ
print(minn)

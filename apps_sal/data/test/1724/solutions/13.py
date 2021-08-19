n = int(input())
a = list(map(int, input().split()))
m = input()
(res, summ) = (0, 0)
for (i, bit) in enumerate(m):
    if bit == '1':
        res = max(res + a[i], summ)
    summ += a[i]
print(res)

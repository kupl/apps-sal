n = int(input())
sum = 0
k = 0
while sum <= n:
    sum += k * (k + 1) // 2
    k += 1
print(k - 2)

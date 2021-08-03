n, m = list(map(int, input().split()))
sum1 = 0
for i in range(n):
    ar = list(map(int, input().split()))
    for j in range(len(ar) - 1):
        if (j % 2 == 0):
            if (ar[j] or ar[j + 1]):
                sum1 += 1
print(sum1)

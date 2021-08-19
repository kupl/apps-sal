n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum = 0
for i in range(n):
    if b[i] > a[i]:
        sum += a[i]
        b[i] -= a[i]
        if b[i] <= a[i + 1]:
            sum += b[i]
            a[i + 1] -= b[i]
        else:
            sum += a[i + 1]
            a[i + 1] = 0
    else:
        sum += b[i]
        a[i] -= b[i]
print(sum)

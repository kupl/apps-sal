n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum = 0
for i in range(n):
    if b[i] > a[i]:
        b[i] -= a[i]
        sum += a[i]
        a[i] = 0
        if b[i] > a[i + 1]:
            sum += a[i + 1]
            a[i + 1] = 0
        else:
            a[i + 1] -= b[i]
            sum += b[i]
    else:
        sum += b[i]
print(sum)

n = int(input())
a = list(map(int, input().split()))
x = 0
for i in range(n):
    if a[i] == 1:
        xm = 2
    else:
        xm = 1
    for j in range(i + 1, n):
        if a[j] - a[j - 1] == 1:
            xm += 1
            if a[j] == 1000:
                xm += 1
        else:
            break
    x = max(x, xm - 2)
print(x)

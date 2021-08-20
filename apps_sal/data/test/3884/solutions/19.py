n = int(input())
m = int(input())
a = list(map(float, input().split()))
b = list(map(float, input().split()))
i = n
f = 0
while i >= 1:
    if a[i - 1] != 1 and b[i - 1] != 1:
        f = 1 / (1 - 1 / a[i - 1]) * (f + m / a[i - 1])
        f = 1 / (1 - 1 / b[i - 1]) * (f + m / b[i - 1])
        i -= 1
    else:
        break
if f <= 10 ** 9 and i == 0:
    print(f)
else:
    print(-1)

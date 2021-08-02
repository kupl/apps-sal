n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = -10000000000; c = 10000000000
for i in range(n):
    if a[i] <= 0:
        b = a[i]
    else:
        c = a[i]
        break
for i in range(n):
    if a[i] < 0 and k > 0:
        a[i] *= -1; k -= 1
    elif a[i] > 0 or k == 0:
        break
if k == 0:
    print(sum(a))
else:
    if b == 0:
        print(sum(a))
    else:
        l = (-1)**k
        if l == -1:
            print(sum(a) - 2 * (min(abs(b), abs(c))))
        else:
            print(sum(a))

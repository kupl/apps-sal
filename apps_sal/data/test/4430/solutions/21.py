n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.reverse()
last = 0
for i in range(n):
    if a[i] > last:
        if m == 0:
            print(i)
            return
        else:
            m -= 1
            last = k - a[i]
    else:
        last -= a[i]
print(n)

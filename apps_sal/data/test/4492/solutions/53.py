n, x = list(map(int, input().split()))
a = [int(i) for i in input().split()]
op = 0
for i in range(1, n):
    s = a[i - 1] + a[i]
    if s > x:
        op += s - x
        if a[i] < s - x:
            a[i] = 0
        else:
            a[i] -= s - x
print(op)

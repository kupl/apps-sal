n, m = map(int, input().split())
a = [1] + list(map(int, input().split()))
time = 0
for i in range(1, m + 1):
    if a[i] >= a[i - 1]:
        time += a[i] - a[i - 1]
    else:
        time += (n - a[i - 1]) + a[i]
print(time)

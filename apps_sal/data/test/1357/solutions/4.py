n, m = map(int, input().split())
a = list(map(int, input().split()))
s = a[0] - 1
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        s += a[i] - a[i - 1]
    elif a[i] < a[i - 1]:
        s += n - a[i - 1] + a[i]
print(s)

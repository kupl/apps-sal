N = int(input())
x = list(map(int, input().split()))
a = sorted(x)
p = int(N / 2) - 1
l = a[p]
for i in range(N):
    n = p
    if x[i] <= l:
        n = p + 1
    print(a[n])

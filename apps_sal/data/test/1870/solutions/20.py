n, c = list(map(int, input().split()))
a = list(map(int, input().split()))

t = 1
for i in range(1, n):
    if a[i] - a[i - 1] > c:
        t = 0
    t += 1
print(t)

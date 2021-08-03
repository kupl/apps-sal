n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
mini = 0
b = []
for i in range(n - 1, n - k - 1, -1):
    b.append(a[i])
b.sort()
print(b[0])

n, m = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

i, j = 0, 0
while i < n and j < m:
    if a[i] <= b[j]:
        i += 1
    j += 1
print(n - i)

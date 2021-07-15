n = int(input())
a = list(map(int, input().split()))
k = 1
m = 0
for i in range(1, n):
    if a[i] >= a[i - 1]:
        k += 1
    else:
        m = max(m, k)
        k = 1
print(max(m, k))


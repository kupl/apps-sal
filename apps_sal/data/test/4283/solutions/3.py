n = int(input())
a = list(map(int, input().split()))
a.sort()
m = 0
i = 0
for j in range(n):
    while a[j] - a[i] > 5:
        i += 1
    m = max(m, j - i + 1)
print(m)

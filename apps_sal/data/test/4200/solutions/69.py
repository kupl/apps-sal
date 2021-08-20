(n, m) = map(int, input().split())
a = list(map(int, input().split()))
count = 0
s = sum(a)
for i in range(n):
    if a[i] >= s / (4 * m):
        count += 1
print('Yes' if count >= m else 'No')

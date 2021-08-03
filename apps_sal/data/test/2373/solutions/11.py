n = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(n - 1):
    if p[i] - 1 == i:
        count += 1
        p[i], p[i + 1] = p[i + 1], p[i]
if p[n - 1] - 1 == n - 1:
    count += 1
print(count)

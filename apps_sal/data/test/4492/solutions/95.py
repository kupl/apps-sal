(n, x) = map(int, input().split())
l = list(map(int, input().split()))
count = 0
for i in range(n - 1):
    if l[i] > x:
        count += l[i] - x
        l[i] -= l[i] - x
    if l[i] + l[i + 1] > x:
        count += l[i] + l[i + 1] - x
        l[i + 1] -= l[i] + l[i + 1] - x
print(count)

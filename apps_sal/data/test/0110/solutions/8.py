n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] >= 0:
        a[i] = -a[i] - 1
if n % 2:
    m = min(a)
    for i in range(n):
        if a[i] == m:
            a[i] = -a[i] - 1
            break
print(*a)

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] >= 0:
        a[i] = -a[i] - 1
x = min(a)

if len(a) % 2 == 1:
    for i in range(n):
        if a[i] == x:
            a[i] = -a[i] - 1
            break
print(*a)

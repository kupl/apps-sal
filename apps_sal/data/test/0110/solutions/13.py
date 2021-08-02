n = int(input())
a = list(map(int, input().split()))

if a == [0]:
    print(0)
    return

for i in range(n):
    if a[i] >= 0:
        a[i] = -a[i] - 1

nbN = len([x for x in a if x < 0])
if n % 2 == 1:
    m = min(a)
    for i in range(n):
        if a[i] == m:
            a[i] = -a[i] - 1
            break

print(*a)

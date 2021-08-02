n = int(input())
a = list(map(int, input().split()))
count = 0
w = False
for i in range(n):
    if a[i] % 2 == 0:
        w = True
    while w:
        count += 1
        a[i] = a[i] // 2
        if a[i] % 2 != 0:
            w = False
print(count)

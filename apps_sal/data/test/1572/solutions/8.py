n = int(input())
a = list(map(int, input().split()))

b = 0
c = 0
for i in range(n - 2):
    if a[i] + a[i + 1] == a[i + 2]:
        c += 1
        if c > b:
            b = c
    else:
        c = 0

if n <= 2:
    print(n)
else:
    print(b + 2)

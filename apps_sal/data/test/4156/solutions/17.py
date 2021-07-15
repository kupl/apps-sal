(n, l) = list(map(int, input().split()))
maxim = 0
min = 0
x = 0
a = list(map(int, input().split()))
for i in range(n):
    x += a[i]
    if x > maxim:
        maxim = x
    if x < min:
        min = x
if (maxim-min) > l:
    print(0)
else:
    print(l-(maxim-min)+1)



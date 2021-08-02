n, x = [int(i) for i in input().split()]
t = 1
k = 0
for i in range(n):
    l, r = [int(y) for y in input().split()]
    while(t + x <= l):
        t += x
    k += r - t + 1
    t = r + 1
print(k)

n = int(input())
hmax = 0
h = [int(i) for i in input().split()]
for i in range(n):
    if h[i] > hmax:
        hmax = h[i]
print(hmax)

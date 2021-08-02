n = int(input())
h = list(map(int, input().split()))
c = 0
d = 0
for i in range(n):
    if h[i] >= d:
        c += 1
        d = h[i]
print(c)

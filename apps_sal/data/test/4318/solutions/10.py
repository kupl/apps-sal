n = int(input())
h = list(map(int, input().split()))
kei = 1
m = h[0]
for i in range(1, n):
    if m <= h[i]:
        m = h[i]
        kei += 1
print(kei)

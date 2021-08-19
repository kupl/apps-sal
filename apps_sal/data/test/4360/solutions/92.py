n = int(input())
a = list(map(int, input().split()))
kei = 0.0
for i in range(n):
    kei += 1 / a[i]
print(float(1 / kei))

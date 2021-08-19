N = int(input())
a = list(map(int, input().split()))
c = [0] * 9
for i in range(N):
    if a[i] >= 3200:
        c[8] += 1
    else:
        for j in range(8):
            if 400 * j <= a[i] and a[i] <= 400 * (j + 1) - 1:
                c[j] = 1
min1 = max(1, sum(c[:8]))
max1 = sum(c)
print(min1, max1)

n = int(input())
h = list(map(int, input().split()))
count = 0
m = 0
for i in range(0, n):
    if i == 0:
        count += 1
        m = h[i]
    elif h[i] >= m:
        count += 1
        m = h[i]
print(count)

n, k = list(map(int, input().split()))
id = [int(i) for i in input().split()]
i = 0
s = i * (i + 1) // 2
while s <= k:
    i += 1
    s = i * (i + 1) // 2

s = (i - 1) * i // 2

k = k - s
if k == 0:
    print(id[i - 2])
else:
    print(id[k - 1])

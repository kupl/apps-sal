(n, k) = input().split()
h = {}
for i in range(int(n)):
    h[int(i) + 1] = 0
for i in range(int(k)):
    input()
    tmp = input().split()
    for j in tmp:
        h[int(j)] += 1
count = 0
for (i, j) in h.items():
    if j == 0:
        count += 1
print(count)

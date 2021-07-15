n = int(input())
l = list(map(int, input().split()))
mask = [0] * 200001
for i in range(n):
    mask[l[i]] += 1
for i in range(200001):
    mask[i] = [mask[i], i]
mask.sort(reverse=True)
cur = mask[0][1]
print(n - mask[0][0])
basis = l.index(cur)
for i in range(basis - 1, -1, -1):
    if l[i] > cur:
        print(2, i + 1, i + 2)
    elif l[i] < cur:
        print(1, i + 1, i + 2)
for i in range(basis + 1, n):
    if l[i] > cur:
        print(2, i + 1, i)
    elif l[i] < cur:
        print(1, i + 1, i)

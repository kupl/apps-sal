
n, v = map(int, input().split(' '))
trees = dict()
count = 0
b_last = 0

for i in range(n):
    a, b = map(int, input().split(' '))
    if trees.get(a):
        trees[a] += b
    else:
        trees[a] = b

m = max(trees.keys())
for i in range(1, m + 2):
    if trees.get(i):
        k = min(v, b_last)
        count += k
        k1 = min(v - k, trees[i])
        count += k1
        b_last = trees[i] - k1
    else:
        count += min(v, b_last)
        b_last = 0

print(count)

s = input().split()
n = int(s[0])
arr = list(map(int, input().split()))
children = [[] for i in range(n + 1)]
for (i, j) in enumerate(arr):
    if 1 < i + 2 <= n:
        children[j].append(i + 2)
leaves = [0] * (n + 1)
for i in range(n, 0, -1):
    if not children[i]:
        leaves[i] = 1
    else:
        leaves[i] = sum((leaves[j] for j in children[i]))
print(' '.join(map(str, sorted(leaves[1:]))))

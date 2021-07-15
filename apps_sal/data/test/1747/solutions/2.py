from collections import defaultdict

n, k = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
D = defaultdict(int)
l = 0
argmax = (0, 0)
for i in range(n):
    D[A[i]] += 1
    if len(D) > k:
        if argmax[1] - argmax[0] < i-1 - l: argmax = (l, i-1)
        while len(D) > k:
            D[A[l]] -= 1
            if D[A[l]] == 0: D.pop(A[l])
            l += 1
if argmax[1] - argmax[0] < n-1 - l: argmax = (l, n-1)
print(argmax[0] + 1, argmax[1] + 1)


N, K = list(map(int, input().split()))

A = list(map(int, input().split()))

ord = [-1 for _ in range(N)]
ord[0] = 0
v = A[0] - 1
root = [0]

while ord[v] == -1:
    ord[v] = len(root)
    root.append(v)

    v = A[v] - 1


l = ord[v]
c = len(root) - l

if K < l:
    ans = root[K]
else:
    K -= l
    K %= c
    ans = root[l + K]
print((ans + 1))

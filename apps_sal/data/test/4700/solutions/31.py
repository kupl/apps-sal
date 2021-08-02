n, m = map(int, input().split())
H = list(map(int, input().split()))
L = [1] * n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if H[a] == H[b]:
        L[a] = 0
        L[b] = 0
    elif H[a] < H[b]:
        L[a] = 0
    elif H[a] > H[b]:
        L[b] = 0
print(sum(L))

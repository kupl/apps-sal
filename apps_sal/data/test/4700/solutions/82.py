n, m = map(int, input().split())
H = list(map(int, input().split()))
L = [1] * n
for _ in range(m):
    a, b = map(int, input().split())
    if H[a - 1] == H[b - 1]:
        L[a - 1] = 0
        L[b - 1] = 0
    elif H[a - 1] < H[b - 1]:
        L[a - 1] = 0
    elif H[a - 1] > H[b - 1]:
        L[b - 1] = 0
print(sum(L))

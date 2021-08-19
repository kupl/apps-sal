N = int(input())
a = [0] + list(map(int, input().split()))
ls = [0] * (N + 1)
for i in range(N, 0, -1):
    sm = 0
    for j in range(i, N + 1, i):
        sm += ls[j]
    ls[i] = sm % 2 ^ a[i]
b = [i for i in range(N + 1) if ls[i] == 1]
print(len(b))
print(*b)

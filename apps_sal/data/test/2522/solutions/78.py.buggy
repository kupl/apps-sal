N, *AB = map(int, open(0).read().split())
A, B = AB[:N], AB[N:]

C = [0] * (N + 1)
D = [0] * (N + 1)

for i, (a, b) in enumerate(zip(A, B)):
    C[a] += 1
    D[b] += 1

if any(c + d > N for c, d in zip(C, D)):
    print("No")
    return

for i in range(1, N + 1):
    C[i] += C[i - 1]
    D[i] += D[i - 1]

x = max(C[i] - D[i - 1] for i in range(1, N + 1))

print("Yes")
print(*[B[(i + N - x) % N] for i in range(N)])

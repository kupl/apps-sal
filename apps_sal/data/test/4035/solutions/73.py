A = [0] * 1301
B = [0] * 1301
for i in range(1, 1301):
    A[i] = int(i * 0.08)
    B[i] = int(i * 0.1)
x, y = map(int, input().split())
X = [s for s, t in enumerate(A) if t == x]
Y = [s for s, t in enumerate(B) if t == y]

for i in X:
    if i in Y:
        print(i)
        return
print(-1)

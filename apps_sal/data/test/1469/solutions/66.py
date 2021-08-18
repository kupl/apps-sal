
L = int(input())

N = 2
while 2**N - 1 <= L - 1:
    N += 1

edge = []
for i in range(1, N):
    edge.append([i, i + 1, 0])
    edge.append([i, i + 1, 2**(i - 1)])

for i in reversed(range(1, N)):
    if L - 2**(i - 1) > 2**(N - 1) - 1:
        edge.append([i, N, L - 2**(i - 1)])
        L = L - 2**(i - 1)

print(N, len(edge))
for x in edge:
    print(*x)

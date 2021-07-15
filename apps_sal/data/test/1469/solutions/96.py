L = int(input())

N = L.bit_length()
n = []
for i in range(1, N):
    n += [[i, i + 1, 0], [i, i + 1, 2**(i - 1)]]
v = 2**(N - 1) - 1
while L - 1 - v > 0:
    b = min(N - 1, (L - 1 - v).bit_length())
    n += [[b, N, v + 1]]
    v += 2**(b - 1)
M = len(n)
print((N, M))
for _ in n:
    print((*_))


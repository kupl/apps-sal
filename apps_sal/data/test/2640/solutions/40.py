import numpy
H, W = map(int, input().split())
S = numpy.array([[1 if i == '.' else 0 for i in input().strip()] for _ in range(H)])
S = numpy.array([S, S])

for w in range(1, W):
    S[0, :, w] += S[0, :, w] * S[0, :, w - 1]
for w in range(W - 2, -1, -1):
    S[0, :, w] = (S[0, :, w] != 0) * numpy.maximum(S[0, :, w], S[0, :, w + 1])
for h in range(1, H):
    S[1, h] += S[1, h] * S[1, h - 1]
for h in range(H - 2, -1, -1):
    S[1, h] = (S[1, h] != 0) * numpy.maximum(S[1, h], S[1, h + 1])

S = S[0] + S[1]
print(numpy.max(S) - 1)

N, A, B = map(int, input().split())
h = [0] * N
for i in range(N):
    h[i] = int(input())

L = 0
R = sum((h[i] - 1) // A + 1 for i in range(N)) + 1
while R - L > 1:
    M = (L + R - 1) // 2 + 1
    count = sum((h[i] - B * M - 1) // (A - B) + 1 for i in range(N) if h[i] - B * M > 0)
    if count > M:
        L = M
    else:
        R = M
print((L + R - 1) // 2 + 1)

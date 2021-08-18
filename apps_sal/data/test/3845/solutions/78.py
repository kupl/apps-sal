
a, b = list(map(int, input().split()))
k = 50
W = [["."] * (k * 2) for i in range(k)]
B = [["

for i in range(b - 1):
    w = (i // k) * 2
    h = (i % k) * 2
    W[w][h] = "


for i in range(a - 1):
    w = (i // k) * 2 + 1
    h = (i % k) * 2 + 1
    B[-w][-h] = "."
ans = [''.join(W[i]) for i in range(k)] + [''.join(B[i]) for i in range(k)]
print((100, 100))
print(('\n'.join(ans)))

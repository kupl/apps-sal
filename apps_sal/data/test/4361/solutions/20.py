n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
h = sorted(h)
H = []

for i in range(n - k + 1):
    H_i = h[i + k - 1] - h[i]
    H.append(H_i)

print(min(H))

(n, k, q) = map(int, input().split())
a = [int(input()) for _ in range(q)]
p = [0] * (n + 1)
for i in a:
    p[i] += 1
for i in range(1, n + 1):
    print('Yes' if p[i] + k - q > 0 else 'No')

(n, k, q) = map(int, input().split())
d = [k - q] * n
for _ in range(q):
    d[int(input()) - 1] += 1
for i in range(n):
    print('Yes' if d[i] > 0 else 'No')

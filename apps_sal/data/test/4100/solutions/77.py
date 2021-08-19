(n, k, q) = map(int, input().split())
a = [0] * n
for i in range(q):
    c = int(input())
    a[c - 1] += 1
for i in range(n):
    print('Yes' if a[i] > q - k else 'No')

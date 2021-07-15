n, k, q = map(int, input().split())
a = [0] * n
for i in range(q):
    p = int(input())
    a[p - 1] += 1
for j in a:
    print('Yes') if k - q + j > 0 else print('No')

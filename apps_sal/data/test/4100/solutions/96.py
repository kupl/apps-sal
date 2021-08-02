n, k, q = map(int, input().split())
a = [0 for i in range(n)]
for i in range(q):
    ai = int(input())
    a[ai - 1] += 1
for i in a:
    if k - q + i > 0:
        print('Yes')
    else:
        print('No')

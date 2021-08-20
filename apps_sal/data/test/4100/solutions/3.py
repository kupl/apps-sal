(n, k, q) = map(int, input().split())
L = list((int(input()) for _ in range(q)))
A = [k - q] * n
for l in L:
    A[l - 1] += 1
for a in A:
    print('Yes' if a > 0 else 'No')

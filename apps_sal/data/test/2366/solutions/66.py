N = int(input())
A = list(map(int, input().split()))
ls = [0] * (N + 1)
for a in A:
    ls[a] += 1
C = 0
for i in set(A):
    n = ls[i]
    C += n * (n - 1) // 2
for a in A:
    n = ls[a]
    print(C - (n - 1))

import bisect
(n, k, c) = map(int, input().split())
c += 1
s = input()
A = [i + 1 for i in range(n) if s[i] == 'o']
L = [1 for i in range(k)]
R = [n for i in range(k)]
for i in range(1, k):
    L[i] = A[bisect.bisect_left(A, L[i - 1] + c)]
    R[-i - 1] = A[bisect.bisect_right(A, R[-i] - c) - 1]
for i in range(k):
    if L[i] == R[i]:
        print(L[i])

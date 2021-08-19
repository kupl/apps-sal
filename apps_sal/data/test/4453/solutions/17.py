N = []
AA = []
t = int(input())
for i in range(t):
    N.append(int(input()))
    a = list(map(int, input().split()))
    for j in range(len(a)):
        a[j] -= 1
    AA.append(a)
for i in range(t):
    n = N[i]
    A = AA[i]
    ans = [0] * n
    for j in range(n):
        c = 1
        b = A[j]
        while b != j:
            b = A[b]
            c += 1
        ans[j] = c
    print(' '.join([str(i) for i in ans]))

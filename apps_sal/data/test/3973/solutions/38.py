(n, m) = map(int, input().split())
a = list(map(int, input().split()))
a0 = a[0]
DDF = [0 for _ in range(m)]
A = [m - 1]
for i in range(1, n):
    A.append((a[i] - a0 - 1) % m)
total_step = 0
for i in range(1, n):
    total_step += (a[i] - a[i - 1]) % m
for i in range(1, n):
    if A[i] > A[i - 1]:
        if A[i - 1] < m - 2:
            DDF[A[i - 1] + 2] += 1
        if A[i] < m - 1:
            DDF[A[i] + 1] -= 1 + (A[i] - A[i - 1]) % m - 1
            if A[i] < m - 2:
                DDF[A[i] + 2] += (A[i] - A[i - 1]) % m - 1
    elif A[i] < A[i - 1]:
        if A[i - 1] < m - 2:
            DDF[A[i - 1] + 2] += 1
        DDF[0] += m - A[i - 1] - 1
        DDF[1] -= m - A[i - 1] - 1 - 1
        if A[i] < m - 1:
            DDF[A[i] + 1] -= 1 + (A[i] - A[i - 1]) % m - 1
            if A[i] < m - 2:
                DDF[A[i] + 2] += (A[i] - A[i - 1]) % m - 1
    '\n  print("DDF @ ", i," : ", DDF) \n  DF = [0 for _ in range(m)]\n  DF[0] = DDF[0]\n  for i in range(1,m):  \n    DF[i] = DF[i-1] + DDF[i]\n  print("DF : ", DF)  \n  F = [0 for _ in range(m)]\n  F[0] = DF[0]\n  for i in range(1,m):  \n    F[i] = F[i-1] + DF[i]\n  print("F : ", F)    \n  '
for i in range(1, m):
    DDF[i] = DDF[i - 1] + DDF[i]
for i in range(1, m):
    DDF[i] = DDF[i - 1] + DDF[i]
print(total_step - max(DDF))

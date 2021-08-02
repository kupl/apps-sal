n, m = map(int, input().split())
a = list(map(int, input().split()))

a0 = a[0]

DDF = [0 for _ in range(m)]  # DF[i] = F[i] - F[i-1], DDF[i] = DF[i] - DF[i-1] (DF[0] = DDF[0] = 0とおく)
A = [m - 1]
for i in range(1, n):
    A.append((a[i] - a0 - 1) % m)
#print("A : ", A)
total_step = 0
for i in range(1, n):
    total_step += (a[i] - a[i - 1]) % m

for i in range(1, n):
    # if A[i] > A[i-1]: DF[A[i-1]+2 : A[i]+1] += 1
    # if A[i] < A[i-1]: DF[A[i-1]+2 : m] += 1; DF[1:A[i]+1] += 1; DF[0] += m-A[i-1]-1
    # DF[A[i]+1] -= (A[i] - A[i-1]) % m - 1
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
        DDF[1] -= (m - A[i - 1] - 1) - 1
        if A[i] < m - 1:
            DDF[A[i] + 1] -= 1 + (A[i] - A[i - 1]) % m - 1
            if A[i] < m - 2:
                DDF[A[i] + 2] += (A[i] - A[i - 1]) % m - 1
    """
  print("DDF @ ", i," : ", DDF) 
  DF = [0 for _ in range(m)]
  DF[0] = DDF[0]
  for i in range(1,m):  
    DF[i] = DF[i-1] + DDF[i]
  print("DF : ", DF)  
  F = [0 for _ in range(m)]
  F[0] = DF[0]
  for i in range(1,m):  
    F[i] = F[i-1] + DF[i]
  print("F : ", F)    
  """

for i in range(1, m):
    DDF[i] = DDF[i - 1] + DDF[i]
#print("DF : ", DDF)
for i in range(1, m):
    DDF[i] = DDF[i - 1] + DDF[i]
#print("F : ", DDF)
print(total_step - max(DDF))

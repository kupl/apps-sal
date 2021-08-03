N = int(input())
A = {}
for i in range(N):
    s = input()
    if s in A:
        A[s] += 1
    else:
        A[s] = 1
s_max = max(A.values())
for j in sorted(k for k in A if A[k] == s_max):
    print(j)

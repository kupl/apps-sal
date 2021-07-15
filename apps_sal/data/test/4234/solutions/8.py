n = int(input())
A = list(input())
u0 = 0
u1 = 1
ans = []
while u1 < n:
    if A[u0] == A[u1]:
        u1 += 1
    else:
        u0 = u1 + 1
        ans.append(A[u1 - 1])
        ans.append(A[u1])
        u1 += 2
print(n - len(ans))
print(''.join(ans))

N = int(input())
A = []
for i in range(N):
    temp = int(input())
    A.append(temp)
# print(A)
L = [A[0]]
for i in range(1, N):
    if L[-1] >= A[i]:
        L.append(A[i])
    else:
        if L[0] < A[i]:
            L[0] = A[i]
        else:
            s = len(L)
            ok = s
            ng = 0
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if L[mid] < A[i]:
                    ok = mid
                else:
                    ng = mid
            L[ok] = A[i]
    # print(L)
ans = len(L)
print(ans)

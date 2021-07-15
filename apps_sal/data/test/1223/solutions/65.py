import bisect
import array
N = int(input())
P = list(map(int, input().split()))
P_id = [0]*(N + 1)

for i in range(N):
    P_id[P[i]] = i

A = array.array('i', [- 1, P_id[N], N])


res = 0
for i in range(N - 1, 0, - 1):
    j = bisect.bisect_left(A, P_id[i])
    A.insert(j, P_id[i])
    l1 = A[j - 1]
    r1 = A[j + 1]
    l2 = l1
    r2 = r1
    if l1 != - 1:
        l2 = A[j - 2]
    if r1 != N:
        r2 = A[j + 2]
    
    res += i*((A[j] - l1)*(r2 - r1) + (l1 - l2)*(r1 - A[j]))

print(res)

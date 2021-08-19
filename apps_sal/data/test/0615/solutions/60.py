import bisect
from collections import deque
n = int(input())
A = list(map(int, input().split()))
S = [A[0]]
for i in range(n - 1):
    S.append(S[-1] + A[i + 1])
ans = 10 ** 15
A1 = deque([A[0]])
A2 = deque(A[1:n])
for i in range(2, n - 1):
    A1.append(A[i - 1])
    A2.popleft()
    if len(A1) == 2:
        M1 = max(A1)
        m1 = min(A1)
    else:
        x = bisect.bisect_left(S, S[i - 1] // 2, lo=0, hi=i + 1)
        M11 = max(S[x - 1], S[i - 1] - S[x - 1])
        m11 = min(S[x - 1], S[i - 1] - S[x - 1])
        M12 = max(S[x], S[i - 1] - S[x])
        m12 = min(S[x], S[i - 1] - S[x])
        M1 = min(M11, M12)
        m1 = max(m11, m12)
    if len(A2) == 2:
        M2 = max(A2)
        m2 = min(A2)
    else:
        x = bisect.bisect_left(S, S[i - 1] + (S[-1] - S[i - 1]) // 2, lo=0, hi=n)
        M21 = max(S[x - 1] - S[i - 1], S[-1] - S[x - 1])
        m21 = min(S[x - 1] - S[i - 1], S[-1] - S[x - 1])
        M22 = max(S[x] - S[i - 1], S[-1] - S[x])
        m22 = min(S[x] - S[i - 1], S[-1] - S[x])
        M2 = min(M21, M22)
        m2 = max(m21, m22)
    a = max(M1, M2) - min(m1, m2)
    if a < ans:
        ans = a
print(ans)

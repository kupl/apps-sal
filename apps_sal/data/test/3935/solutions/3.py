import sys
from collections import Counter
readline = sys.stdin.readline

N = int(input())
A = list(map(int, readline().split()))
B = [(a & -a).bit_length() for a in A]
C = Counter(B).most_common(1)[0][0]
Ans = []
for i in range(N):
    if C != B[i]:
        Ans.append(A[i])

print(len(Ans))
if Ans:
    print(*Ans)

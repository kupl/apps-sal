from collections import Counter
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
R = C.most_common()[0][0]
op = []
l = A.index(R)
r = l
l -= 1
r += 1
while l >= 0:
    if A[l] == R:
        l -= 1
        continue
    elif A[l] < R:
        op.append([1, l + 1, l + 2])
    else:
        op.append([2, l + 1, l + 2])
    l -= 1
while r < N:
    if A[r] == R:
        r += 1
        continue
    elif A[r] < R:
        op.append([1, r + 1, r])
    else:
        op.append([2, r + 1, r])
    r += 1
if len(op):
    print(len(op))
    for l in op:
        print(*l)
else:
    print(len(op))

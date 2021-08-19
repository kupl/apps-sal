import sys
import collections
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = []
C = []
for (i, a) in enumerate(A):
    B.append(i + a)
    C.append(i - a)
cnt = 0
Bc = collections.Counter(B)
Cc = collections.Counter(C)
for (key, val) in list(Bc.items()):
    cnt += val * Cc[key]
print(cnt)

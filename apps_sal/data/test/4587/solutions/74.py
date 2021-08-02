import bisect

N = int(input())
b1 = 0
d = 0

ans = 0

A = list(map(int, input().split()))
A = sorted(A)
B = list(map(int, input().split()))
B = sorted(B, reverse=True)
C = list(map(int, input().split()))
C = sorted(C)
D = []
E = []

for b in B:
    d = d + len(C) - bisect.bisect_right(C, b)
    D.append(d)

D = sorted(D, reverse=True)
B = sorted(B)

for a in A:
    if 0 <= bisect.bisect_right(B, a) <= len(D) - 1:
        ans += D[bisect.bisect_right(B, a)]
print(ans)

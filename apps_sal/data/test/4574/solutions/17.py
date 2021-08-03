import collections
N = int(input())
L = list(map(int, input().split()))
c = collections.Counter(L)
A = list(c.keys())
B = list(c.values())
R = list()
for i in range(len(A)):
    if B[i] >= 2:
        R.append([A[i], B[i]])
R = sorted(R, reverse=True)
if len(R) == 0:
    print(0)
    return
if R[0][1] >= 4:
    print(R[0][0]**2)
elif len(R) < 2:
    print(0)
else:
    print(R[0][0] * R[1][0])

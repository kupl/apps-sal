N = int(input())
A = list(map(int,input().split()))
import collections
a = collections.Counter(A)
b = []
for i, j in a.items():
    if j >= 2:
        b.append([i,j])
b.sort(reverse=True)
if len(b) >= 1 and b[0][1] >= 4:
    print(b[0][0] ** 2)
elif len(b) >= 2:
    print(b[0][0] * b[1][0])
else:
    print(0)

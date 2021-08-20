from collections import Counter
n = int(input())
list_A = list(map(int, input().split()))
(L, R) = ([], [])
for i in range(n):
    if i % 2 == 0:
        L.append(list_A[i])
    else:
        R.append(list_A[i])
A = Counter(L)
A = sorted(list(A.items()), key=lambda x: x[1], reverse=True)
A.append((-1, 0))
B = Counter(R)
B = sorted(list(B.items()), key=lambda x: x[1], reverse=True)
B.append((-1, 0))
if A[0][0] != B[0][0]:
    print(n - A[0][1] - B[0][1])
else:
    print(min(n - A[1][1] - B[0][1], n - A[0][1] - B[1][1]))

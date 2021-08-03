from collections import Counter
n = int(input())
V = list(map(int, input().split()))
x = len(set(V))
if x == 1:
    print((n // 2))
else:
    A = list()
    B = list()
    for i, v in enumerate(V):
        if i & 1:
            A.append(v)
        else:
            B.append(v)
    A = Counter(A).most_common()
    B = Counter(B).most_common()
    a = A[0]
    b = B[0]
    if a[0] == b[0]:
        if len(A) == 1:
            b = B[1]
        elif len(B) == 1:
            a = A[1]
        else:
            if A[1][1] >= B[1][1]:
                a = A[1]
            else:
                b = B[1]
    print((n - a[1] - b[1]))

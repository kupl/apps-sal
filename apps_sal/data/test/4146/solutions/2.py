import collections
N = int(input())
v = list(map(int, input().split()))
(v1, v2) = (v[::2], v[1::2])
A1 = collections.Counter(v1)
A2 = collections.Counter(v2)
B = list(A1.values())
C = list(A2.values())
B.sort(reverse=True)
C.sort(reverse=True)
if A1.most_common()[0][0] == A2.most_common()[0][0]:
    if len(A1) == 1:
        ans = N // 2
    elif B[1] > C[1]:
        ans = N // 2 - B[0] + N // 2 - B[1]
    else:
        ans = N // 2 - B[0] + N // 2 - C[1]
else:
    ans = N // 2 - B[0] + N // 2 - C[0]
print(ans)

from collections import Counter
import copy


def LI():
    return list(map(int, input().split()))


N = int(input())
A = LI()
B = Counter(A)
A = copy.copy(B)

for k, v in B.items():

    if k - 1 in A:
        A[k - 1] += v
    else:
        A[k - 1] = v
    if k + 1 in A:
        A[k + 1] += v
    else:
        A[k + 1] += v

print(max(A.values()))

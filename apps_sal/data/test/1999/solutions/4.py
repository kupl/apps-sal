from collections import deque

N = int(input())
A = list(map(int, input().split()))

# index = [-1] * (sum(A)+1)
#
# for i in range(N):
#     while index[A[i]] != -1:
#         A[index[A[i]]] = -1     # -1 は delete
#         index[A[i]] = -1        # A[i] はなくなった
#         A[i] *= 2
#     index[A[i]] = i

dic = dict()

for i in range(N):
    while A[i] in dic:
        A[dic[A[i]]] = -1     # -1 は delete
        del dic[A[i]]        # A[i] はなくなった
        A[i] *= 2
    dic[A[i]] = i

B = []
for a in A:
    if a > 0:
        B.append(a)
print(len(B))
print(" ".join(list(map(str, B))))

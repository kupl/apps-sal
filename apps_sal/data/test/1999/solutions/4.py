from collections import deque

N = int(input())
A = list(map(int, input().split()))


dic = dict()

for i in range(N):
    while A[i] in dic:
        A[dic[A[i]]] = -1
        del dic[A[i]]
        A[i] *= 2
    dic[A[i]] = i

B = []
for a in A:
    if a > 0:
        B.append(a)
print(len(B))
print(" ".join(list(map(str, B))))

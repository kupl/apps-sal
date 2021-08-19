# 166 B
N, K = list(map(int, input().split()))
A = []
for i in range(K):
    d = int(input())
    a = []
    if d > 1:
        a = list(map(int, input().split()))
        A.extend(a)
    else:
        A.append(int(input()))

print(N - len(set(A)))

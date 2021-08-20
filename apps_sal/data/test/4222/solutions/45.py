(N, K) = map(int, input().split())
d = [0 for _ in range(K)]
A = [[] for _ in range(K)]
for i in range(K):
    d[i] = int(input())
    A[i] = list(map(int, input().split()))
su_list = [i for i in range(1, N + 1)]
for i in range(K):
    for j in range(d[i]):
        if A[i][j] in su_list:
            su_list.remove(A[i][j])
print(len(su_list))

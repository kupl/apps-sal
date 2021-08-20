(K, N) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = []
for i in range(len(A) - 1):
    B.append(A[i + 1] - A[i])
B.append(A[0] - A[N - 1] + K)
b_max = max(B)
b_max_index = B.index(max(B))
B.remove(b_max)
print(sum(B))

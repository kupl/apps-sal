n = int(input())
A = list(map(int, input().split()))
B = [(i+1, A[i]) for i in range(n)]
B.sort(key=lambda x: x[1])
print (" ".join(list(map(str, [B[i][0] for i in range(n)]))))

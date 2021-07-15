N,M = map(int,input().split())
A = list(map(int,input().split()))
B = [list(map(int,input().split())) for _ in range(M)]
B.sort(key = lambda x:x[1])
B = list(reversed(B))
A.sort()

num = 0
for i in range(M):
    for j in range(B[i][0]):
        if num > N-1:
            break
        if A[num] < B[i][1]:
            A[num] = B[i][1]
            num += 1
        else:
            break

print(sum(A))

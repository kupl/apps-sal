N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
temp = 1
V = []
for i in range(N - 1):
    if A[i] == A[i + 1]:
        temp += 1
    else:
        V.append(temp)
        temp = 1

V.append(temp)
V.sort()
ans = N - sum(V[-K:])
print(ans)

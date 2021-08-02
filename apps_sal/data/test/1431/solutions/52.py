N = int(input())
A = list(map(int, input().split()))
ans = [0] * N
index = []
M = 0
for i in range(N - 1, -1, -1):
    a = ans[i:N:i + 1]
    if sum(a) % 2 == A[i]:
        ans[i] = 0
    else:
        ans[i] = 1
        index.append(i + 1)
        M += 1
print(M)
print(*index[::-1])

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = sorted(A)
ans = []
flag = 0
for i in range(N - K + 1):
    ans.append(B[i + K - 1] - B[i])
    flag = 1
print(min(ans) if flag == 1 else "0")

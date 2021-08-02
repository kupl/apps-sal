N = int(input())
C = list(map(int, input().split()))
ans = 0
for i in range(N - 1, 0, -1):
    if C[i] != C[0]:
        ans = max(ans, i)
        break
for i in range(N - 1):
    if C[i] != C[-1]:
        ans = max(ans, N - 1 - i)
print(ans)

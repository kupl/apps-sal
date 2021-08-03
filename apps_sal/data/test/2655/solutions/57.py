N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

ans = 0
for i in range(1, N):
    ans += A[i // 2]
print(ans)

N = int(input())
A = list(map(int, input().split()))

ans = 0
max_num = 0

for i in range(N):
    max_num = max(max_num, A[i])
    bi = max_num
    ans += bi - A[i]

print(ans)

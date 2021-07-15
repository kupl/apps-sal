N = int(input())
A = list(map(int, input().split()))+[0]

su = 0
ans = 0
right = 0

for left in range(N):
    while (left == right or su+A[right] == su^A[right]) and right < N:
        su += A[right]
        right += 1
    ans += right-left
    su -= A[left]
print(ans)

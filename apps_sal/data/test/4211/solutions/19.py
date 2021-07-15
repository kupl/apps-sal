N = int(input())
B = input().split()

ans = 0

for i in range(N):
    if i == 0:
        ans += int(B[i])
    elif i == N-1:
        ans += int(B[i-1])
    else:
        ans += min(int(B[i]),int(B[i-1]))

print(ans)

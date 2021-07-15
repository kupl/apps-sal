N = int(input())
A = list(map(int, input().split()))

ans = float('inf')
for i in range(N):
    temp = 0
    while A[i] % 2 == 0:
        A[i] /= 2
        temp += 1
    ans = min(ans, temp)

print(ans)


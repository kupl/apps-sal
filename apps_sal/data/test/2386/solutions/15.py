N = int(input())
A = input().split(' ')
B = []
for i in range(N):
    B.append(int(A[i]) - (i + 1))
B.sort()
ans = 0
for i in range(N):
    ans += abs(int(A[i]) - (B[N // 2] + i + 1))
print(ans)

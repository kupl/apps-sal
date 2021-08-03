N = int(input())
A = []
for _ in range(2):
    A.append(list(map(int, input().split())))
ans = 0
for i in range(N):
    tmp = 0
    tmp += sum(A[0][:i + 1])
    tmp += sum(A[1][i:])
    if tmp > ans:
        ans = tmp
print(ans)

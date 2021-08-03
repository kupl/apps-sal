N = int(input())
A = list(map(int, input().rstrip().split(" ")))
A.sort()
ans = N
for i in range(N - 1):
    if A[i] == A[i + 1]:
        ans -= 1
if ans % 2 == 0:
    ans -= 1
print(ans)

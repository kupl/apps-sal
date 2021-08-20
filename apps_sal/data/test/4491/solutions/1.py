N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(1, N + 1):
    ans = max(sum(A[:i]) + sum(B[i - 1:]), ans)
print(ans)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    change1 = min(A[i], B[i])
    ans += change1
    A[i] -= change1
    B[i] -= change1
    change2 = min(A[i + 1], B[i])
    ans += change2
    A[i + 1] -= change2
    B[i] -= change2
print(ans)

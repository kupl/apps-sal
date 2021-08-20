N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
B.append(0)
ans = 0
for i in range(N + 1):
    taosukazu1 = min(A[i], B[i])
    B[i] -= taosukazu1
    A[i] -= taosukazu1
    ans += taosukazu1
    if B[i] > 0:
        taosukazu2 = min(A[i + 1], B[i])
        B[i] -= taosukazu2
        A[i + 1] -= taosukazu2
        ans += taosukazu2
print(ans)

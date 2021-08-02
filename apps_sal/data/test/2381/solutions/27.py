N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

A_neg = []
A_pos = []

for i in range(N):
    if A[i] <= 0:
        A_neg.append(-A[i])
    else:
        A_pos.append(A[i])

A_neg.sort(reverse=True)
A_pos.sort(reverse=True)

ans = 1

if K == N:
    for i in range(N):
        ans *= (A[i] % 1000000007)
        ans %= 1000000007
    print(ans)

elif K % 2 == 1 and len(A_pos) == 0:
    for i in range(1, K + 1):
        ans *= ((-A_neg[-i]) % 1000000007)
        ans %= 1000000007
    print(ans)

else:
    if K % 2 == 1:
        ans *= A_pos.pop(0)
        K -= 1
    buf = []
    for i in range(len(A_pos) // 2):
        buf.append(A_pos[2 * i] * A_pos[2 * i + 1])
    for i in range(len(A_neg) // 2):
        buf.append(A_neg[2 * i] * A_neg[2 * i + 1])
    buf.sort(reverse=True)
    for i in range(K // 2):
        ans *= (buf[i] % 1000000007)
        ans %= 1000000007
    print(ans)

A, B = map(int, input().split())
C = A
D = B
for i in range(B):
    K = C % D
    if K == 0:
        break
    else:
        C = D
        D = K
ans = (A * B) // D
print(ans)

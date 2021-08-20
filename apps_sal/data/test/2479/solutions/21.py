(N, Q) = map(int, input().split())
HW = [N, N]
ans = (N - 2) ** 2
L_HW = [[N - 2 for i in range(N)] for j in range(2)]
for _ in range(Q):
    (vh, x) = map(int, input().split())
    vh -= 1
    if x > HW[1 - vh]:
        ans -= L_HW[1 - vh][x]
    else:
        L_HW[1 - vh][x + 1:HW[1 - vh]] = [HW[vh] - 2] * (HW[1 - vh] - x - 1)
        HW[1 - vh] = x
        ans -= HW[vh] - 2
print(ans)

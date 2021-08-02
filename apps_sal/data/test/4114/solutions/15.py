N = int(input())

Info = [[] for T in range(0, N)]
for I in range(0, N):
    Info[I] = [int(T) for T in input().split()]
Info = sorted(Info, reverse=True, key=lambda X: X[2])
for CX in range(0, 101):
    for CY in range(0, 101):
        Flag = True
        BaseH = abs(Info[0][0] - CX) + abs(Info[0][1] - CY) + Info[0][2]
        for I in range(1, N):
            if max(BaseH - abs(Info[I][0] - CX) - abs(Info[I][1] - CY), 0) != Info[I][2]:
                Flag = False
                break
        if Flag:
            Ans = [str(CX), str(CY), str(BaseH)]
            break
    if Flag:
        break
print(' '.join(Ans))

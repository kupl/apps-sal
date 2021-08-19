N = int(input())
Nums = list(map(int, input().split()))
Good = [1] * (N * 2)
Amounts = [0] * 100
(Mono, Duo) = (0, 0)
for Num in Nums:
    if Amounts[Num] == 0:
        Mono += 1
    elif Amounts[Num] == 1:
        Duo += 1
        Mono -= 1
    Amounts[Num] += 1
Flag = Mono % 2
Duo_Flag = False
Counts = [0] * 100
for i in range(2 * N):
    Num = Nums[i]
    if Amounts[Num] == 1:
        if Flag:
            Good[i] = 1
        else:
            Good[i] = 2
        Flag = not Flag
    else:
        if Counts[Num] == 0:
            Good[i] = 1
        elif Counts[Num] == 1:
            Good[i] = 2
        else:
            if Duo_Flag:
                Good[i] = 1
            else:
                Good[i] = 2
            Duo_Flag = not Duo_Flag
        Counts[Num] += 1
print((Duo + Mono // 2) * (Duo + (Mono + 1) // 2))
print(*Good)

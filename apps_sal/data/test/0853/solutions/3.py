N = int(input())
Numbers = list(map(int, input().split()))
Zeros, Fives = 0, 0
for Num in Numbers:
    if Num == 0:
        Zeros += 1
    else:
        Fives += 1
if Zeros == 0:
    print(-1)
elif Fives < 9:
    print(0)
else:
    print("5" * (Fives // 9 * 9) + "0" * Zeros)


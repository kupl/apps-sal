K = int(input())
wa = 0
kake = 1
for i in range(1, K + 1):
    if i != 1:
        kake = kake * 10 % K
    wa += 7 * kake
    if wa % K == 0:
        print(i)
        return
print(-1)

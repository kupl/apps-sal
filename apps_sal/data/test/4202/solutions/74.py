L, R = map(int, input().split())
Dif = abs(L - R) + 1
if Dif >= 2020:
    Ans = 0
else:
    Box = []
    for i in range(L, R + 1):
        Box.append(i % 2019)
    Box.sort()
    Ans = 2020 * 2020
    for i in range(len(Box) - 1):
        B1 = Box[i]
        for j in range(i + 1, len(Box)):
            B2 = Box[j]
            Ans = min((B1 * B2) % 2019, Ans)
print(Ans % 2019)

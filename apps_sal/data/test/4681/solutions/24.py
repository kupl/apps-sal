n = int(input())
Luca = [0] * 100
Luca[0] = 2
Luca[1] = 1
for i in range(2, n + 1):
    Luca[i] = Luca[i - 1] + Luca[i - 2]
print(Luca[n])

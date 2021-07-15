S = input().strip()
Words = S.split('bear')
N = len(S)
Amount = (N * (N + 1)) // 2
if len(Words) > 1:
    K = len(Words[0]) + 3
    Amount -= (K * (K + 1)) // 2
    K = len(Words[-1]) + 3
    Amount -= (K * (K + 1)) // 2
    for i in range(1, len(Words) - 1):
        K = len(Words[i]) + 6
        Amount -= (K * (K + 1)) // 2
    Amount += 3 * (len(Words) - 1)
    print(Amount)
else:
    print(0)


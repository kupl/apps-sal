S = input()
N = len(S)
K = int(input())
StringList = []
for TSt in range(0, N):
    for TEd in range(TSt + 1, TSt + K + 1):
        StringList.append(S[TSt:TEd])
SetString = sorted(set(StringList))
print(SetString[K - 1])

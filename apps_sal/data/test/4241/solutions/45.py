S = input()
T = input()
lenS = len(S)
lenT = len(T)
MIN = float('inf')
for i in range(lenS):
    tmpS = S[i:i+lenT]
    if len(tmpS) != lenT:
        continue
    count = 0
    for i in range(lenT):
        if tmpS[i] != T[i]:
            count += 1
    MIN = min(MIN,count)
print(MIN)

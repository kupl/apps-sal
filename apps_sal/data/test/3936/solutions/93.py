N = int(input())

Mod = 10**9 + 7
S = input()
T = input()

if S[0] == T[0]:
    K, I = 3, 1
    Mode = True
else:
    K, I = 6, 2
    Mode = False


while I < N:
    if S[I] == T[I]:
        if Mode:
            K *= 2
        else:
            K *= 1
        Mode = True
        I += 1
    else:
        if Mode:
            K *= 2
        else:
            K *= 3
        Mode = False
        I += 2
    K %= Mod
print(K)

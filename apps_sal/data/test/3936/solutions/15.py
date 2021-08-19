from collections import Counter
n = int(input())
S = input()
Do = Counter(S)
Ans = 0
i = 0
if Do[S[0]] == 1:
    Ans = 3
    i += 1
    sig = 1
else:
    Ans = 6
    i += 2
    sig = 2
while not i >= n:
    if Do[S[i]] == 1:
        if sig == 1:
            Ans *= 2
        else:
            Ans *= 1
        sig = 1
        i += 1
    else:
        if sig == 1:
            Ans *= 2
        else:
            Ans *= 3
        sig = 2
        i += 2
    Ans = Ans % (10 ** 9 + 7)
print(Ans)

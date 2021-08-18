import itertools
N = str(input())
Keta = len(N)
N_List = ["3", "5", "7"]

Ans = 0
for i in range(3, Keta):
    Ans += 3**i
    Ans -= (2**i * 3) - 3

N = int(N)

if Keta >= 3:
    for Moji in itertools.product(N_List, repeat=Keta):
        Moji_Kazu = len(set(Moji))
        Str_Number = int("".join(Moji))
        if (Str_Number <= N) & (Moji_Kazu == 3):
            Ans += 1

print(Ans)

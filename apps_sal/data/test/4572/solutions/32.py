S = input()

alph = "abcdefghijklmnopqrstuvwxyz"

for i in alph:
    if i in S:
        alph = alph.replace(i, "")

if len(alph) == 0:
    print("None")
else:
    print(alph[0])

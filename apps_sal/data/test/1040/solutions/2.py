N = int(input())
S = input()
T = ""
for s in S:
    if s in "fox":
        T += s
        if T[-3:] == "fox":
            T = T[:-3]
            N -= 3
    else:
        T = ""
print(N)

S = input()
T = input()
D = 0
for i in range(len(S)):
    if S[i] != T[i]:
        D += 1
print(D)

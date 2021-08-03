S = input()
T = input()
p = 0

for i in range(0, len(S)):
    if S[i] == T[i]:
        pass
    else:
        p += 1

print(p)

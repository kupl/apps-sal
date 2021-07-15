S = list(input())
T = list(input())
c = 0
for i in range(3):
    if S[i] == T[i]:
        c += 1
print(c)

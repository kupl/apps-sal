S = input()
T = input()

res = 0
for i in range(3):
    if S[i] == T[i]:
        res += 1

print(res)

S = input()
k = 0
for i in range(len(S)):
    if S[i] == "o":
        k = k + 1
print(700 + 100 * k)

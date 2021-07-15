S = input()
T = input()
count = 0
for i in range(len(S)):
    if S[i] != T[i]:
        count = count + 1
print(count)

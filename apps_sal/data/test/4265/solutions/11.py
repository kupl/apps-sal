S = input()
T = input()
l = len(S)
count = 0
for i in range(l):
    if S[i] != T[i]:
        count += 1
print(count)

S = input()

c = 0
l = len(S)

for i in range(l):
    if S[i] == str(i % 2):
        c += 1

print(min(c, l-c))

S = input() + '_'
x = -2
y = -2
for n in range(len(S) - 2):
    if S[n] == S[n + 1]:
        x = n
        y = n + 1
    if S[n] == S[n + 2]:
        x = n
        y = n + 2
print(x + 1, y + 1)

S = input()
x = abs(753 - int(S[0] + S[1] + S[2]))

for i in range(1, len(S) - 2):
    n = S[i] + S[i + 1] + S[i + 2]
    x = min(x, abs(753 - int(n)))

print(x)

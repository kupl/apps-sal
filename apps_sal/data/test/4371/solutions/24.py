S = input()

lists = []
S_len = len(S)

for i in range(0, S_len - 2):
    X = int(S[i] + S[i + 1] + S[i + 2])
    lists.append(abs(X - 753))

print(min(lists))

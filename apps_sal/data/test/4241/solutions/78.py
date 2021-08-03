S = input()
T = input()
ma = 0
match = 0
for i in range(len(S) - len(T) + 1):
    match = 0
    for j in range(len(T)):
        if S[i + j] == T[j]:
            match += 1
    ma = max(ma, match)
print(len(T) - ma)

S = str(input())
S = S[:-2]

for _ in range(len(S) // 2):

    if S[:len(S) // 2] == S[len(S) // 2:]:
        print(len(S))
        break

    else:
        S = S[:-2]

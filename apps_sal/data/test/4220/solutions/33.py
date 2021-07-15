K = int(input())
S = input()

if len(S) <= K:
    print(S)
else:
    string = S[0:K] + "..."
    print(string)

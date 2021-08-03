N, K = map(int, input().split())
S = input()
for i in range(K):
    S = S + S
    t = ""
    for j in range(0, 2 * N, 2):
        if (S[j] == "R" and (S[j + 1] == "S" or S[j + 1] == "R")) or (S[j] == "S" and S[j + 1] == "R"):
            t += "R"
        elif (S[j] == "S" and (S[j + 1] == "S" or S[j + 1] == "P")) or (S[j] == "P" and S[j + 1] == "S"):
            t += "S"
        else:
            t += "P"
    S = t
print(S[0])

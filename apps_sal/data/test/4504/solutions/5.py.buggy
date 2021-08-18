import sys
S = input()
ans = 0


for i in range(len(S) // 2):
    S = S[:len(S) - 2]
    # print(S)
    count = 0
    for j in range(len(S) // 2):
        if S[j] != S[len(S) // 2 + j]:
            break
        else:
            count += 1
    if count == len(S) // 2:
        print((len(S)))
        return

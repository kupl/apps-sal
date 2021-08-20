S = [int(i) for i in input()]
K = int(input())
if sum(S) == len(S):
    print(1)
else:
    for i in range(len(S)):
        if S[i] != 1:
            print(S[i])
            break
        elif S[i] == 1 and K - 1 <= i:
            print(1)
            break

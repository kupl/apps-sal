S = input()
N = len(S)
for i in range((N - 1) // 2, 0, -1):
    if S[0:i] == S[i:2 * i]:
        print((2 * i))
        break

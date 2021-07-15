S = input()
for i in range(2, len(S)+2, 2):
    split = int(len(S[:-i])/2)
    if S[:split] == S[split:-i]:
        print((len(S[:-i])))
        return


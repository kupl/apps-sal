
S = input()
T = input()

for i in range(len(S)):
    S = S[1:] + S[0]
    if T == S:
        print('Yes')
        break
else:
    print('No')

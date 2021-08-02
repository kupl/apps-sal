S = input()
T = input()

for i in range(len(S)):
    x = S[-i:] + S[:-i]
    if x == T:
        print('Yes')
        break
else:
    print('No')

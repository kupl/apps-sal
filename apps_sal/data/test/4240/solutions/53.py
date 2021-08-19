S = str(input())
T = str(input())
for i in range(len(S)):
    if S[i:] + S[:i] == T:
        print('Yes')
        break
else:
    print('No')

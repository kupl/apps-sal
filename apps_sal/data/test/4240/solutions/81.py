S = str(input())
T = str(input())
a = len(S)
for i in range(0, a):
    if S[i:] + S[:i] == T:
        print('Yes')
        break
else:
    print('No')

S = input()

for i in range(len(S)):
    if S[i] in S[i+1:]:
        print('no')
        break
else:
    print('yes')

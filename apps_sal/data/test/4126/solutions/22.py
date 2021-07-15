S = list(input())
S1 = S[:(len(S)-1)//2]
S1 = S[(len(S)+1)//2:]
if S == list(reversed(S)):
    if S1 == list(reversed(S1)):
        print('Yes')
    else:
        print('No')
else:
    print('No')

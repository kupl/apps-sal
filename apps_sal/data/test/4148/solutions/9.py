al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = int(input())
S = list(input())
for i in range(len(S)):
    S[i] = al[al.index(S[i]) + N]
print(''.join(S))

from sys import stdin, stdout
input()
S = list(input())
ct = 0
for i in range(0, len(S), 2):
    if S[i] == S[i + 1]:
        ct += 1
        if S[i] == 'a':
            S[i] = 'b'
        else:
            S[i] = 'a'
print(ct)
print(''.join(S))

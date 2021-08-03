S = input()
N = len(S)

if S != S[::-1]:
    print('No')
elif S[:(N - 1) // 2] != (S[:(N - 1) // 2])[::-1]:
    print('No')
elif S[(N + 3) // 2 - 1:] != (S[(N + 3) // 2 - 1:])[::-1]:
    print('No')
else:
    print('Yes')

N = int(input())
S = input()
if N % 2 == 1:
    print('No')
    return
if S[:int(N / 2)] == S[int(N / 2):]:
    print('Yes')
else:
    print('No')

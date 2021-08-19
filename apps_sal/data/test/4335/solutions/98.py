N = int(input())
S = input()
if N % 2 != 0:
    print('No')
elif S[:int(N / 2)] == S[int(N / 2):]:
    print('Yes')
else:
    print('No')

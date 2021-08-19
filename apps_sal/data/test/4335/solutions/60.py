N = int(input())
S = input()
if N % 2 > 0 or S != S[:int(N / 2)] + S[:int(N / 2)]:
    print('No')
else:
    print('Yes')

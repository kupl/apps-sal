N = int(input())
S, T = input().split()

words = [S, T]
for i in range(N):
    print(''.join([S[i]+T[i]]), end='')


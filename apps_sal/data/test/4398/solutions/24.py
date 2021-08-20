N = int(input())
(S, T) = input().split()
for i in range(N):
    print(''.join([S[i] + T[i]]), end='')

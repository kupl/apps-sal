(N, K) = map(int, input().split())
S = list(input())
if S[K - 1] == 'A':
    S[K - 1] = 'a'
if S[K - 1] == 'B':
    S[K - 1] = 'b'
if S[K - 1] == 'C':
    S[K - 1] = 'c'
for i in S:
    print(i, end='')

(N, K) = map(int, input().split())
S = input()
if S[K - 1] == 'A':
    rep = 'a'
elif S[K - 1] == 'B':
    rep = 'b'
else:
    rep = 'c'
print(S[:K - 1] + rep + S[K:])

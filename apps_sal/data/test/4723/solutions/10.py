S = input()
T = input()
(L, M) = (len(S), len(T))
a = -1
for i in range(L - M, -1, -1):
    if sum([1 for j in range(M) if S[i + j] == '?' or S[i + j] == T[j]]) == M:
        a = i
        break
print('UNRESTORABLE' if a < 0 else ''.join([T[i - a] if a <= i < a + M else 'a' if S[i] == '?' else S[i] for i in range(L)]))

input()
S = input()

print(1 + sum(s1 != s2 for s1, s2 in zip(S, S[1:])))

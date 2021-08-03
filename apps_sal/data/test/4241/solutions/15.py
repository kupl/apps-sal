S, T = open(0)
print(min(sum(c != d for c, d in zip(S[i:], T[:-1]))for i in range(len(S) - len(T) + 1)))

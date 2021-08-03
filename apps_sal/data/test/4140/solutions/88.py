S = input()
A = S[0::2].count("1") + S[1::2].count("0")
B = S[0::2].count("0") + S[1::2].count("1")

print(min(A, B))

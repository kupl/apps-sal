S = input()
z = S.count("0")
o = S.count("1")

print(len(S) - abs(z - o))

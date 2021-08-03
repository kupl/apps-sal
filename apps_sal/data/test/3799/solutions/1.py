S = input()
flag = (S[0] != S[-1]) ^ (len(S) % 2 == 0)
print(("First" if flag else "Second"))

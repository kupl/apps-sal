S = input()
l = len(S)
print(('First' if (l & 1) ^ (S[0] == S[-1]) else 'Second'))

S = input()
A = len(S) % 2
B = 0 if S[0] == S[-1] else 1
print('Second' if A ^ B else 'First')

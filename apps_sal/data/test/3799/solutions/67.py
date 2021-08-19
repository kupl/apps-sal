S = input().rstrip()
print('First' if (len(S) + (S[0] == S[-1])) % 2 else 'Second')

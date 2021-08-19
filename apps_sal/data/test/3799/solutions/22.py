S = input()
start_end = S[0] == S[-1]
odd = len(S) % 2
print('First' if start_end and (not odd) or (not start_end and odd) else 'Second')

S = input().strip()
if S[0] == S[-1]:
    print('First' if len(S) % 2 == 0 else 'Second')
else:
    print('Second' if len(S) % 2 == 0 else 'First')

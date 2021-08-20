def check(string):
    if string == string[::-1]:
        return True
    else:
        return False


S = input()
n = len(S)
S1 = S[:(n - 1) // 2]
S2 = S[(n + 1) // 2:]
if check(S) and check(S1) and check(S2):
    print('Yes')
else:
    print('No')

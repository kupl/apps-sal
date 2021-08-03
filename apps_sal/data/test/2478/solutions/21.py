n = int(input())
S = input()
T = S.replace('()', '')
for _ in range(50):
    T = T.replace('()', '')
print('(' * T.count(')') + S + ')' * T.count('('))

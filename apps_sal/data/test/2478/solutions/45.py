N = int(input())
S = input()
T = S
for n in range(N):
    T = T.replace('()', '')
L = T.count('(')
R = T.count(')')
S = R * '(' + S + L * ')'
print(S)

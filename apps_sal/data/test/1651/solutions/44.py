S, P = map(int, input().split())
r = (S**2 - 4 * P)**(1 / 2)
M1 = (S + r) / 2
M2 = (S - r) / 2
N1 = S - M1
N2 = S - M2
if (M1 % 1 == 0 and 1 <= M1 < S) or (M2 % 1 == 0 and 1 <= M1 < S):
    print('Yes')
else:
    print('No')

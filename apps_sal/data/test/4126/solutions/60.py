S1 = input()
N = len(S1)
S2 = S1[::-1]
a = S1 == S2
S3 = S1[:int((N - 1) / 2)]
S4 = S3[::-1]
b = S3 == S4
S5 = S1[int((N + 3) / 2) - 1:]
S6 = S5[::-1]
c = S5 == S6
if a and b and c:
    print('Yes')
else:
    print('No')

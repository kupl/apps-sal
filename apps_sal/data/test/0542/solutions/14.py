X = int(input())
E = []
F = []
S = []
for I in range(X):
    t = int(input())
    if t > 0:
        F.append(t)
    else:
        S.append(-t)
    E.append(t)
if sum(F) > sum(S):
    print('first')
elif sum(F) < sum(S):
    print('second')
else:
    a = [int(x) for x in F]
    b = [int(x) for x in S]
    if a > b:
        print('first')
    elif a < b:
        print('second')
    elif E[-1] > 0:
        print('first')
    else:
        print('second')

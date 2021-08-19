import collections
N = int(input())
O = []
E = []
A = list([int(a) for a in input().split(' ')])
for i in range(N):
    if i % 2 == 0:
        E.append(A[i])
    else:
        O.append(A[i])
CE = collections.Counter(E)
CO = collections.Counter(O)
CE2 = CE.most_common(2)
CO2 = CO.most_common(2)
if CE2[0][0] != CO2[0][0]:
    print(len(E) + len(O) - CE2[0][1] - CO2[0][1])
elif CE2[0][0] == CO2[0][0]:
    if len(CE2) == 1 and len(CO2) == 1:
        print(min([CE2[0][1], CO2[0][1]]))
    elif len(CE2) > 1 and len(CO2) == 1:
        print(len(E) + len(O) - CE2[1][1] - CO2[0][1])
    elif len(CE2) == 1 and len(CO2) > 1:
        print(len(E) + len(O) - CE2[0][1] - CO2[1][1])
    elif CE2[0][1] + CO2[1][1] > CO2[0][1] + CE2[1][1]:
        print(len(E) + len(O) - CE2[0][1] - CO2[1][1])
    elif CE2[0][1] + CO2[1][1] <= CO2[0][1] + CE2[1][1]:
        print(len(E) + len(O) - CE2[1][1] - CO2[0][1])

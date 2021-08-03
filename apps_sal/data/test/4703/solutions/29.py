from itertools import product
S = input()
if len(S) == 1:
    print(int(S))
else:
    Sum = 0
    for TR in product([0, 1], repeat=(len(S) - 1)):
        Op = ['+' if TO == 1 else '' for TO in TR] + ['']
        Sum += eval(''.join([TS + TO for TS, TO in zip(S, Op)]))
    print(Sum)

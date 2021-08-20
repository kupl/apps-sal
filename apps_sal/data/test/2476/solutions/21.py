import sys
import collections as cl
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
c = cl.Counter(A)
NumberTupleList = c.most_common()
NumberList = [x[1] for x in NumberTupleList[::-1]]
LengthOfNumberList = len(NumberList)
FormulaList = [0 for i in range(N)]
flag = 0
S = sum(NumberList)
for x in range(1, N + 1):
    while flag < LengthOfNumberList and NumberList[flag] <= x:
        flag += 1
    if flag < LengthOfNumberList:
        FormulaList[x - 1] = (sum(NumberList[:flag]) + x * (LengthOfNumberList - flag)) / x
    else:
        FormulaList[x - 1] = S / x
pin = N - 1
for K in range(1, N + 1):
    while pin >= 0 and K > FormulaList[pin]:
        pin -= 1
    print(pin + 1)

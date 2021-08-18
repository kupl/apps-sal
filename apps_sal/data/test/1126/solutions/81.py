import sys

input = sys.stdin.readline

N, X, M = map(int, input().split())
LIST = [X]
SET = {X}

a = X

while True:
    if a * a % M in SET:
        break
    else:
        a = a * a % M
        LIST.append(a)
        SET.add(a)

start = LIST.index(a * a % M)
LEN = len(LIST)

if N <= LEN:
    print(sum(LIST[:N]))
else:
    LoopTimes, Excess = divmod(N - LEN, LEN - start)
    LoopSum = sum(LIST[start:]) * LoopTimes
    ExSum = sum(LIST[start:start + Excess])
    print(sum(LIST[:]) + LoopSum + ExSum)

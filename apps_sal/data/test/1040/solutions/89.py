import sys
readline = sys.stdin.readline
N = int(readline())
S = readline().rstrip()
T = ''
for s in S:
    T += s
    if len(T) >= 3 and T[-3:] == 'fox':
        T = T[:-3]
print(len(T))

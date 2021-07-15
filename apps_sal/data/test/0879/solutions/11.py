import sys
n = int(sys.stdin.readline())
P = [0,0] + [int(i) for i in sys.stdin.readline().strip().split()]

i = n
s = [n]
while i != 1:
    s.append(P[i])
    i = P[i]
    
print(' '.join([str(i) for i in reversed(s)]))


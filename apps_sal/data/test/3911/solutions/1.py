import sys
3
n = int(sys.stdin.readline().rstrip())
A = []
for i in range(n):
    A.append(1)
    while len(A) >= 2 and A[-1] == A[-2]:
        A.pop()
        A[-1] += 1
print(' '.join(map(str, A)))

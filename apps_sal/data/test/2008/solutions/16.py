import sys
N = int(input())
alu = 0
A = []
B = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    alu += min(a, b)
    if a < b:
        B.append(b - a)
    else:
        A.append(a - b)
alu *= (N-1)
A.sort(reverse = True)
B.sort(reverse = True)
alu += sum([i*j for i, j in enumerate(A)]) + sum([i*j for i, j in enumerate(B)])
print(alu)

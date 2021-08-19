(N, H) = map(int, input().split())
K = [list(map(int, input().split())) for n in range(N)]
A = max((k[0] for k in K))
B = sorted((b for (a, b) in K if A < b))
C = 0
while 0 < H and B:
    H -= B.pop()
    C += 1
print(C - -max(0, H) // A)

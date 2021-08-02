import math
N = int(input())
C = str(input())

C = C.replace('W', '1').replace('R', '0')
C = list(C)
sort_C = sorted(C)

cnt = 0

for i in range(N):
    if C[i] != sort_C[i]:
        cnt += 1

print(math.ceil(cnt / 2))

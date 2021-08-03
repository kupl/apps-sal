A, B = list(map(int, input().split()))
C, D, s = 0, 0, B - A + 1
C = 0 if A % 2 == 0 else A
D = 0 if B % 2 == 1 else B
if ((s - (0 if C == 0 else 1) - (0 if D == 0 else 1)) // 2) % 2 == 0:
    E = 0
else:
    E = 1
print((C ^ D ^ E))

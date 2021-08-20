3
(NA, NB) = list(map(int, input().split()))
WA = {input() for _ in range(NA)}
WB = {input() for _ in range(NB)}
Wcomm = WA & WB
C = len(Wcomm)
A = NA - C
B = NB - C
A += C % 2
if A > B:
    print('YES')
else:
    print('NO')

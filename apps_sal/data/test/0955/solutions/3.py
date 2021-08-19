def mi():
    return map(int, input().split())


n = int(input())
a = [0] * n
for i in range(n):
    a[i] = list(input().split())
    a[i][0] = int(a[i][0])
(A, B, C, AB, AC, BC, ABC) = (10000000000.0, 10000000000.0, 10000000000.0, 10000000000.0, 10000000000.0, 10000000000.0, 10000000000.0)
for i in range(n):
    a[i][1] = ''.join(sorted(list(a[i][1])))
    if a[i][1] == 'A':
        A = min(A, a[i][0])
    if a[i][1] == 'AB':
        AB = min(AB, a[i][0])
    if a[i][1] == 'AC':
        AC = min(AC, a[i][0])
    if a[i][1] == 'BC':
        BC = min(BC, a[i][0])
    if a[i][1] == 'ABC':
        ABC = min(ABC, a[i][0])
    if a[i][1] == 'B':
        B = min(B, a[i][0])
    if a[i][1] == 'C':
        C = min(C, a[i][0])
t = [AB + C, AB + AC, AB + BC, AB + ABC, BC + A, BC + AB, BC + AC, BC + ABC, AC + B, AC + AB, AC + BC, AC + ABC, ABC, A + B + C]
lol = min(t)
if lol == 10000000000.0:
    print(-1)
else:
    print(lol)

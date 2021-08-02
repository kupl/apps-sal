N, M = map(int, input().split())
A = set()
B = set()
for i in range(M):
    a, b = input().split()
    if a == '1':
        A.add(b)
    if b == str(N):
        B.add(a)
if A & B:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')

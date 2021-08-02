A, B, C = list(map(int, input().split()))
clear = 0

for i in range(1, B):
    if (A * i) % B == C:
        clear = 1
        break

if clear == 0:
    print('NO')
else:
    print('YES')

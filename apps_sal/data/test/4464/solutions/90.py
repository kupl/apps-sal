A, B, C = list(map(int, input().split()))
calc = 0

for i in range(1000):
    calc += A
    rem = calc % B
    if rem == C:
        print('YES')
        return

print('NO')


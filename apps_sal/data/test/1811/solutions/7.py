n, jump = list(map(int, input().split()))
rocks = 0
for i, ch in enumerate(input()):
    if ch == '#':
        rocks += 1
        if rocks == jump:
            print('NO')
            import sys; return
    else:
        rocks = 0
print('YES')


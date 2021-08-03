3

s = input()

if len(s) % 2 != 0:
    print(-1)
else:
    dy = s.count('U') - s.count('D')
    dx = s.count('R') - s.count('L')
    print((abs(dx) + abs(dy)) // 2)

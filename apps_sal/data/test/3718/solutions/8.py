_ = input()
balls = sorted(list(set([int(x) for x in input().split()])))
for i in range(len(balls) - 2):
    a = balls[i]
    b = balls[i + 2]
    if b - a <= 2:
        print('YES')
        break
else:
    print('NO')

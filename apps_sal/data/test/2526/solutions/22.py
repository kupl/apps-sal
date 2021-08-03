X, Y, A, B, C = list(map(int, input().split()))
p = sorted(list(map(int, input().split())), reverse=True)
q = sorted(list(map(int, input().split())), reverse=True)
r = sorted(list(map(int, input().split())), reverse=True)

red = p[:X]
green = q[:Y]

red_no_eat = 0
green_no_eat = 0
for no in r:
    red_worst = red[-red_no_eat - 1] if red_no_eat < X else 10 ** 10
    green_worst = green[-green_no_eat - 1] if green_no_eat < Y else 10 ** 10
    if no > red_worst or no > green_worst:
        if red_worst < green_worst:
            red_no_eat += 1
        else:
            green_no_eat += 1
print((sum(p[:X - red_no_eat]) + sum(q[:Y - green_no_eat]) + sum(r[:red_no_eat + green_no_eat])))

a, b = list(map(int, input().split(':')))
c, d = list(map(int, input().split(':')))
t = a * 60 + b - c * 60 - d

if t < 0:
    t += 60 * 24
a, b = t // 60, t % 60

print(str(a // 10) + str(a % 10) + ':' + str(b // 10) + str(b % 10))

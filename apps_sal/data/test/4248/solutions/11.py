n = int(input())
theta = 5.0
for i in range(n):
    theta += list(map(float, input().split()))[1] / n
print('%.3f' % theta)

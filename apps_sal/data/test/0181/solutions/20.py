n = int(input())

t = n - (n // 360) * 360
i = 0
while not (-45 <= t <= 45 or 315 <= t <= 360):
    i += 1
    t -= 90
print(i)

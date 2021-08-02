a, b, t = map(int, input().split())
bis = 0
for i in range(1, 30):
    time = a * i
    if time < t + 0.5:
        bis += b
print(bis)

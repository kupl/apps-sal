
x, t = map(int, input().split())

weight = 0
if x > t:
    weight = x - t
else:
    weight = 0

print(weight)

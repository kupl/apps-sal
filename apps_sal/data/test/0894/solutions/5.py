s = input()
x = int(s.split()[0])
y = int(s.split()[1])
absl = abs(x) + abs(y)
if (x > 0):
    if (y > 0):
        print(0, absl, absl, 0)
    else:
        print(0, -absl, absl, 0)
else:
    if (y > 0):
        print(-absl, 0, 0, absl)
    else:
        print(-absl, 0, 0, -absl)

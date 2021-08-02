count = int(input())
x = 0
for i in range(0, count):
    raw = input()
    if '--' in raw:
        x -= 1
    else:
        x += 1
print(x)

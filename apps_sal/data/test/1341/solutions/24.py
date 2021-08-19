pole = input()
commands = input()
curX = 0
for c in commands:
    if c == pole[curX]:
        curX += 1
print(curX + 1)

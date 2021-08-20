n = int(input())
over = []
speed = []
for x in range(n):
    ab = input()
    if len(ab) > 1:
        (a, b) = ab.split()
    else:
        a = ab
    if a == '1' or a == '3' or a == '5':
        if a == '5':
            speed.append([5, 2 ** 31 - 1])
        else:
            speed.append([int(a), int(b)])
    else:
        over.append(int(a))
overignore = 0
oversum = 0
i = len(over) - 1
while i >= 0:
    if over[i] == 2:
        oversum += 1
    elif over[i] == 4:
        oversum = 0
    if over[i] == 6 and oversum > 0:
        overignore += 1
    i -= 1
curspeed = []
stack = []
stack.append(2 ** 31 - 1)
i = 0
while i < len(speed):
    if speed[i][0] == 1:
        curspeed.append(speed[i][1])
    else:
        curspeed.append(curspeed[-1])
        stack.append(speed[i][1])
    i += 1
speedignore = 0
i = len(speed) - 1
while i >= 0:
    if speed[i][0] != 1 and speed[i][1] == stack[-1]:
        if curspeed[i] > stack[-1]:
            stack.pop()
            speedignore += 1
        else:
            stack.pop()
            i -= 1
    elif curspeed[i] > stack[-1]:
        stack.pop()
        speedignore += 1
    else:
        i -= 1
print(speedignore + overignore)

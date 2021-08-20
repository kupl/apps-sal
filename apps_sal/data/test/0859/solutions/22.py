__author__ = 'hamed1soleimani'
correct = input()
received = input()
final = 0
for ch in correct:
    if ch == '+':
        final += 1
    else:
        final -= 1
directions = [0]
for ch in received:
    if ch == '+':
        for i in range(len(directions)):
            directions[i] += 1
    elif ch == '-':
        for i in range(len(directions)):
            directions[i] -= 1
    else:
        temp = list()
        for d in directions:
            temp.append(d + 1)
            temp.append(d - 1)
        directions = temp
finished = 0
for d in directions:
    if d == final:
        finished += 1
out = str(finished / len(directions))
out += '0' * (14 - len(out))
print(out)

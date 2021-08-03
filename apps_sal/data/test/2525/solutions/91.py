from collections import deque
s = deque(list(input()))
n = int(input())
count = 0


for i in range(n):
    x = input()
    if x[0] == "1":
        count += 1
        count %= 2

    elif x[2] == "1":
        if count % 2 == 0:
            s.appendleft(x[4])
        else:
            s.append(x[4])
    else:
        if count % 2 == 0:
            s.append(x[4])
        else:
            s.appendleft(x[4])


if count % 2 == 1:
    s.reverse()

print("".join(s))

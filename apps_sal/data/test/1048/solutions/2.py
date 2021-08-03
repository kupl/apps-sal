n = int(input())
instructions = input()
left = 0
right = 0
up = 0
down = 0
for i in instructions:
    if i == "L":
        left += 1
    elif i == "R":
        right += 1
    elif i == "U":
        up += 1
    elif i == "D":
        down += 1
print((min(left, right) + min(up, down)) * 2)

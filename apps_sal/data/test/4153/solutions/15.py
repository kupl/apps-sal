import sys

cubes = list(input())
stack = []
count = 0

for cube in cubes:
    if not stack:
        stack.append(cube)
    elif stack[-1] != cube:
        count += 2
        stack.pop()
    else:
        stack.append(cube)
print(count)

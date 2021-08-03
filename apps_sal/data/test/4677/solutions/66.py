s = input()

stack = []

for c in s:
    if c == "B":
        if len(stack) == 0:
            continue
        else:
            stack.pop(-1)
    else:
        stack.extend(c)
for c in stack:
    print(c, end="")

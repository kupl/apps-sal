stack = []
counter = 0
possible = True
for b in input():
    if b in "{<([":
        stack.append(b)
    else:
        if not stack:
            possible = False
            break
        popped = stack.pop()
        if (b == "}" and popped != "{") or \
            (b == ">" and popped != "<") or \
            (b == ")" and popped != "(") or \
                (b == "]" and popped != "["):
            counter += 1

if possible and not stack:
    print(counter)
else:
    print("Impossible")

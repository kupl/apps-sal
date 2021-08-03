info = input().split(',')
info = [(word, int(num)) for word, num in zip(info[::2], info[1::2])]
out = []
stack = []
for index, item in enumerate(info):
    level = len(stack)
    while level > 0 and stack[-1] == 0:
        stack.pop()
        level -= 1

    if len(out) <= level:
        out.append([item[0]])
    else:
        out[level].append(item[0])

    if item[1] > 0:
        stack.append(item[1])

    if level > 0:
        stack[level - 1] -= 1

print(len(out))
print('\n'.join(' '.join(line) for line in out))

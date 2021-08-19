n = int(input())
widths = [(int(x), c) for (c, x) in enumerate(input().split())]
widths.sort()
passengers = input()
seating = ''
stack = []
i = 0
for pi in passengers:
    if pi == '1':
        seating += str(stack[-1][1] + 1) + ' '
        stack.pop()
    else:
        stack.append(widths[i])
        seating += str(stack[-1][1] + 1) + ' '
        i += 1
print(seating[:-1])

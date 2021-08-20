levels = []
left = [-1]
inp = input().split(',')
i = 0
while i < len(inp):
    if len(levels) <= len(left) - 1:
        levels.append([])
    t = inp[i]
    n = int(inp[i + 1])
    levels[len(left) - 1].append(t)
    if n > 0:
        left.append(n)
    while left[-1] == 0:
        del left[-1]
    left[-1] -= 1
    i += 2
print(len(levels))
for i in levels:
    print(' '.join(i))

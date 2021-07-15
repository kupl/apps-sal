import sys


s = sys.stdin.readline().strip().split(",")
n = len(s) // 2
levels = [[]]
stack = []
for i in range(n):
    st = s[i * 2]
    if (len(stack) + 1 > len(levels)):
        levels.append([])
    levels[len(stack)].append(st)
    if (len(stack)):
        stack[-1] -= 1
    nm = int(s[i * 2 + 1])
    stack.append(nm)
    while (len(stack) and stack[-1] == 0):
        stack.pop()
sys.stdout.write("{}\n".format(len(levels)) + '\n'.join([' '.join(x) for x in levels]) + '\n')
sys.stdout.flush()






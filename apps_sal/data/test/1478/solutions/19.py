ls = [[] for _ in range(10 ** 6 // 4)]
maxd = 0
s = input().split(',')
i = 0
stack = [1000000]
for i in range(0, len(s), 2):
    (w, c) = (s[i], int(s[i + 1]))
    ls[len(stack) - 1].append(w)
    stack[-1] -= 1
    stack.append(c)
    while stack[-1] == 0:
        stack.pop()
    maxd = max(maxd, len(stack))
print(maxd)
for i in range(maxd):
    print(*ls[i])

# coding=utf-8

n = int(input())

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

c = [[[[0, 0]], [], [], []], [[[0, 1], [1, 0]], [[1, 1]], [], []], [[[0, 2], [2, 0]], [], [[2, 2]], []], [[[0, 3], [1, 2], [2, 1], [3, 0]], [[1, 3], [3, 1]], [[2, 3], [3, 2]], [[3, 3]]]]

stack = c[a[0]][b[0]][:]

i = 1

while i < n - 1 and stack:
    helper = c[a[i]][b[i]][:]
    for e in helper:
        j = 0
        while j < len(stack):
            if stack[j][-1] == e[0] and len(stack[j]) == i + 1:
                stack[j].append(e[1])
            j += 1

    j = 0
    while j < len(stack):
        if len(stack[j]) == i + 1:
            del stack[j]
        else:
            j += 1
    i += 1

if stack:
    print('YES')
    print(*stack[0])
else:
    print('NO')

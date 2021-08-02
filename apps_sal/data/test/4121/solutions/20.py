n = int(input())
a = [i for i in map(int, input().split(' '))]
mx = max(a)
stack = [a[0]]
for i in range(1, n):
    if len(stack) != 0:
        if a[i] % 2 == stack[-1] % 2:
            stack.pop()
        else:
            stack.append(a[i])
    else:
        stack.append(a[i])
if len(stack) > 1:
    print('NO')
else:
    print('YES')

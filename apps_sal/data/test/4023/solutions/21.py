n = int(input())
a = [i for i in map(int, input().split(' '))]
mx = max(a)
stack = [a[0]]
q = True
for i in range(1, n):
    if len(stack) != 0:
        if a[i] == stack[-1]:
            stack.pop()
        elif a[i] > stack[-1]:
            q = False
            break
        else:
            stack.append(a[i])
    else:
        stack.append(a[i])
if len(stack) > 1 or (len(stack) == 1 and stack.pop() != mx):
    q = False
if q:
    print('YES')
else:
    print('NO')

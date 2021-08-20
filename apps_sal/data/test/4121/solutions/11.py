n = int(input())
arr = list(map(int, input().split()))
arr = list([x % 2 for x in arr])
stack = []
for i in range(n):
    if len(stack):
        if stack[-1] == arr[i]:
            stack.pop()
        else:
            stack.append(arr[i])
    else:
        stack.append(arr[i])
if len(stack) == 0 or len(stack) == 1:
    print('YES')
else:
    print('NO')

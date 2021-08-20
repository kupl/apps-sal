n = int(input())
s = input()
stack = []
ans = 0
for i in range(n):
    if s[i] == 'f':
        stack.append('f')
    elif s[i] == 'o':
        stack.append('o')
    elif s[i] == 'x':
        if len(stack) >= 2:
            if stack[-1] == 'o' and stack[-2] == 'f':
                ans += 1
                stack.pop()
                stack.pop()
            else:
                stack.clear()
        else:
            stack.clear()
    else:
        stack.clear()
print(n - ans * 3)

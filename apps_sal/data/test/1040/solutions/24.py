ans = int(input())
S = input()
stack = []
for c in S:
    stack.append(c)
    if 3 <= len(stack) and stack[-3] == 'f' and stack[-2] == 'o' and stack[-1] == 'x':
        stack.pop()
        stack.pop()
        stack.pop()
        ans -= 3
print(ans)

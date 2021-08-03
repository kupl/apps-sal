n = int(input())
a = input()
stack, ans = [], []
for q in range(len(a)):
    if a[q] == ')':
        ans.append(stack.pop())
    elif len(stack) > 0 and stack[-1] == '0':
        stack.append('1')
        ans.append('1')
    else:
        stack.append('0')
        ans.append('0')
print(''.join(ans))

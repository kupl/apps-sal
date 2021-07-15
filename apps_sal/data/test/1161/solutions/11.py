s = input()

stack = []
answer = 0
corrects = ('[]', '{}', '<>', '()')
for i in s:
    if i == '[' or i == '{' or i == '<' or i == '(':
        stack.append(i)
    else:
        if len(stack) == 0:
            print('Impossible')
            return
        else:
            top = stack.pop()
            if top + i not in corrects:
                answer += 1

print(answer if len(stack) == 0 else 'Impossible')


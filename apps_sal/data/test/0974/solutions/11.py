n = int(input())
pointer = 1
series = [0] * n
stack = []

reset = 0
for i in range(1, (n * 2) + 1):
    inp = input().split(' ')
    if inp[0] == 'add':
        number = int(inp[1])
        stack.append(number)
    if inp[0] == 'remove':
        if len(stack) == 0:
            pointer += 1
        elif stack[-1] == pointer:
            del stack[-1]
            pointer += 1
        else:
            reset += 1
            stack = []
            pointer += 1
print(reset)

n_boxes = int(input())
stack = []
b = 1
count = 0
for i in range(2 * n_boxes):
    input_string = input().split(' ')
    if len(input_string) == 2:
        x = int(input_string[1])
        stack.append(x)
    else:
        if len(stack) != 0:
            if stack[-1] == b:
                stack.pop()
            else:
                count += 1
                stack = []
        b += 1
print(count)

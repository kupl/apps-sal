n = int(input())
a = [int(x) for x in input().split()]
stack = []
i = 0
x = a[i]
while True:
    if len(stack) == 0:
        stack.append(x)
        i += 1
        if i == n:
            break
        x = a[i]
    else:
        if x == stack[-1]:
            del stack[-1]
            x += 1
        else:
            stack.append(x)
            i += 1
            if i == n:
                break
            x = a[i]
print(len(stack))
print(" ".join([str(x) for x in stack]))



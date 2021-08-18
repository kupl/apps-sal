
input()
stack1 = [int(i) for i in input().split()]
stack1.reverse()

stack2 = []

while stack1:
    transfer = stack1.pop()

    while stack2 and stack2[-1] == transfer:
        stack2.pop()
        transfer += 1

    stack2.append(transfer)

print(len(stack2))
print(" ".join([str(i) for i in stack2]))

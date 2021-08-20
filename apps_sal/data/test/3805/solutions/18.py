def Untangled(exp):
    stack = []
    for i in exp:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    return 'No' if stack else 'Yes'


exp = input().strip()
print(Untangled(exp))

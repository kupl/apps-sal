n = int(input())
s = input()

stack = []

for i in range(n):
    stack.append(s[i])
    while stack[-3:] == ['f', 'o', 'x']:
        stack.pop()
        stack.pop()
        stack.pop()

print(len(stack))

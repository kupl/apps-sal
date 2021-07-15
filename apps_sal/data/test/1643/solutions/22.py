s = input()
t = list(s)
stack =[]
for i in range(len(s)):
    if t[i]=='1':
        stack.append(i)
    elif len(stack):
        stack.pop()

for i in range(len(stack)):
    t[stack[i]] = '0'
print(''.join(t))

s = input()
n = len(s)
stack = []
c = 0
for i in range(n):
    if stack and stack[-1] == s[i]:
        stack.pop()
        c += 1
    else:
        stack.append(s[i])
if c % 2 == 1:
    print('Yes')
else:
    print('No')

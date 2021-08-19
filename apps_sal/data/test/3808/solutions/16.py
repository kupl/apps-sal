n = int(input())
seq = list(input())
stack = 0
minstack = 0
for i in seq:
    if i == '(':
        stack += 1
    else:
        stack -= 1
    if stack < minstack:
        minstack = stack
if stack == 0 and minstack >= -1:
    print('Yes')
else:
    print('No')

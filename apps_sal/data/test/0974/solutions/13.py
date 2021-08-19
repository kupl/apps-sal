ans = 0
num = 1
stack = []
n = int(input())
for i in range(2 * n):
    s = input()
    if s.find('add') != -1:
        stack.append(int(s.split()[1]))
    else:
        if len(stack) != 0 and stack[-1] != num:
            stack = []
            ans += 1
        if len(stack):
            stack.pop()
        num += 1
print(ans)

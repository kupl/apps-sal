N = int(input())
s = list(input())
stack = []
cnt = 0
for i in range(N):
    if s[i] == "f":
        stack.append("f")
    elif s[i] == "o" and len(stack) >= 1:
        if not stack[-1] == "f":
            stack = []
        else:
            stack.append("o")
    elif s[i] == "x" and len(stack) >= 2:
        if stack[-2] == "f" and stack[-1] == "o":
            stack.pop()
            stack.pop()
            cnt += 1
        else:
            stack = []
    else:
        stack = []
print((N - 3 * cnt))

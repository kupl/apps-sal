S = input()
stack = []
cnt = 0
for s in S:
    if not stack:
        stack.append(s)
    elif stack[-1] != s:
        stack.pop()
        cnt += 2
    else:
        stack.append(s)
print(cnt)

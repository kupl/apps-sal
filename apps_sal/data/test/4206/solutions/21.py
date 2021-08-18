s = input()
ans = 0
stack = ""
revStack = ""
cursor = 0
for e in s:
    if e == "0":
        ans += 1
        stack = ""
    elif int(e) % 3 == 0:
        ans += 1
        stack = ""
    else:
        stack += e
        if (int(stack) % 3 == 0):
            ans += 1
            stack = ""
        elif len(stack) > 2:
            cursor = -1
            revStack = ""
            while -cursor < len(stack):
                revStack = stack[cursor] + revStack
                if int(revStack) % 3 == 0:
                    ans += 1
                    stack = ""
print(ans)

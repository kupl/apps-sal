n = int(input())
front = {}
back = {}
reg = 0
for i in range(n):
    stk = []
    s = input()
    for char in s:
        if len(stk) == 0:
            stk.append(char)
        elif char == ")" and stk[-1] == "(":
            t = stk.pop()
        else:
            stk.append(char)
    if len(stk) == 0:
        reg += 1
    else:
        if stk == [")"] * len(stk):
            try:
                front[len(stk)] += 1
            except:
                front[len(stk)] = 1
        elif stk == ["("] * len(stk):
            try:
                back[len(stk)] += 1
            except:
                back[len(stk)] = 1
ans = reg ** 2
for k, v in list(front.items()):
    try:
        ans += v * back[k]
    except:
        pass
print(ans)

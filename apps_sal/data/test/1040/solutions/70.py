n = int(input())
s = input()

stk = []
cnt = 0
for i in s:
    if i in ["f", "o", "x"]:
        stk.append(i)
    else:
        stk = []

    if i == "x":
        if len(stk) >= 3 and stk[-1] == "x" and stk[-2] == "o" and stk[-3] == "f":
            stk.pop()
            stk.pop()
            stk.pop()
            cnt += 1

print(n - 3 * cnt)

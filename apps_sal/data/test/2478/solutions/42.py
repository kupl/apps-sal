n = int(input())
s = input()

a = ""

stack = []

for i in range(len(s)):
    if s[i] == "(":
        stack.append("(")
        a += "("
    elif s[i] == ")" and len(stack) == 0:
        stack.append(")")
        a += ")"
    elif s[i] == ")" and stack[-1] == ")":
        stack.append(")")
        a += ")"
    else:  # s[i] == ")" and stack[-1] == "("
        stack.pop(-1)
        a += ")"

while len(stack) > 0:
    if stack[len(stack) - 1] == ")":
        e = len(stack) - 1
        s = e
        while s - 1 >= 0 and stack[s - 1] == ")":
            s -= 1
        a = "(" * (e - s + 1) + a
        stack = stack[:s]
    elif stack[len(stack) - 1] == "(":
        e = len(stack) - 1
        s = e
        while s - 1 >= 0 and stack[s - 1] == "(":
            s -= 1
        a = a + ")" * (e - s + 1)
        stack = stack[:s]

print(a)

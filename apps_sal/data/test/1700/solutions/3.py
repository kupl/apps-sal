n = int(input())

s = input()

red, blue = 0, 0
ans = [0 for _ in range(n)]

for i, item in enumerate(s):
    if item == '(':
        if red == blue:
            red += 1
            ans[i] = 0
        else:
            blue += 1
            ans[i] = 1
    elif item == ')':
        if red == blue:
            blue -= 1
            ans[i] = 1
        else:
            red -= 1
            ans[i] = 0

print(''.join(list(map(str, ans))))

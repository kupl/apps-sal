s = input()
ans = []
count = 0
last_pos = s.rfind('#')
for i, c in enumerate(s):
    if c == '(':
        count += 1
    elif c == ')':
        count -= 1
    elif c == '#' and i == last_pos:
        num = max(1, s.count('(') * 2 - len(s) + 1)
        count -= num
        ans.append(num)
    else:
        count -= 1
        ans.append(1)
    if count < 0:
        print(-1)
        break
else:
    for t in ans:
        print(t)

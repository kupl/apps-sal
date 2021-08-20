s = input()
d = []
ans = 0
for f in s:
    if f in '{[<(':
        d.append(f)
    elif f == ')' and d and (d[-1] == '('):
        d.pop()
    elif f == '}' and d and (d[-1] == '{'):
        d.pop()
    elif f == ']' and d and (d[-1] == '['):
        d.pop()
    elif f == '>' and d and (d[-1] == '<'):
        d.pop()
    elif not d:
        print('Impossible')
        break
    else:
        ans += 1
        d.pop()
else:
    if not d:
        print(ans)
    else:
        print('Impossible')

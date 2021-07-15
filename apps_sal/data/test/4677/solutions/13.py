s = input()

ans = ""
for c in s:
    if c == '0':
        ans += c
    elif c == '1':
        ans += c
    else: # c == 'B'
        if ans != "":
            ans = ans[:-1]

print(ans)

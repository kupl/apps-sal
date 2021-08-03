s = input()
ans = ""
for char in s:
    if char != 'B':
        ans += char
    else:
        if ans == "":
            pass
        else:
            le = len(ans)
            ans = ans[0:le - 1]
print(ans)

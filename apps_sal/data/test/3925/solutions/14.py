s = input()
c = 1
mx = 1
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        c += 1
    elif s[0] != s[-1]:
        s = s[:i + 1][::-1] + s[i + 1:][::-1]
        c += 1
    else:
        if c > mx:
            mx = c
        c = 1
print(max(mx, c))

x = input()
x = list(x)
i = 0
ans = 0
out = ans
while i != len(x):
    if i == 0:
        if x[i] == 'R':
            ans = 1
            out = ans
    elif x[i] == x[i - 1]:
        if x[i] == 'R':
            ans += 1
            out = max(ans, out)
        else:
            ans = 0
    elif x[i] == 'R':
        ans = 1
        out = max(ans, out)
    else:
        ans = 0
    i += 1
print(out)

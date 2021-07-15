s = input()
t = mx = 0
for i in s:
    if i == '-' and t > 0:
        t -= 1
    elif i == '+':
        t += 1
        mx = max(mx, t)
    else:
        mx += 1
print(mx)

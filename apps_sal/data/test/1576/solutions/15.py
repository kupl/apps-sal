t = input()
ans = ''
while len(t) > 0:
    if len(t) % 2 == 0:
        ans = t[-1] + ans
        t = t[:-1]
    else:
        ans = t[0] + ans
        t = t[1:]
print(ans)

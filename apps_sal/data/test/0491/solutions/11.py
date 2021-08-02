s = input()
ans = int(s)
if s[0] == '-' and len(s) >= 2:
    if len(s) == 2:
        ans = 0
    else:
        ans = max(int(s[:-1]), int(s[:-2] + s[-1]), ans)
print(ans)

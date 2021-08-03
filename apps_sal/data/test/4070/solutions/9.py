x = int(input())
s = hex(x).split('x')[-1]
ans = 0
for c in s:
    if c in '0469ad':
        ans += 1
    elif c in '8b':
        ans += 2
print(ans)

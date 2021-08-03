ans = True
s = 2
for c in input().strip():
    if c == '1':
        s = 0
    elif c == '4':
        s += 1
        if s >= 3:
            ans = False
    else:
        ans = False

print("YES" if ans else "NO")

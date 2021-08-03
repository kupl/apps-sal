ans = 0
for c in input():
    if c == 'A':
        ans += 1
    elif c == '1':
        ans += 10
    else:
        ans += int(c)
print(ans)

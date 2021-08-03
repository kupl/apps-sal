v, ans = 0, ''
for c in input()[::-1]:
    if c == '0' or v:
        ans += c
        v += (1 if c == '1' else -1)
    else:
        ans += '0'
print(ans[::-1])

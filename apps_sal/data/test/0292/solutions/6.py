(h, n) = map(int, input().split(' '))
ans = 0
left = True
for i in range(h):
    ch = h - i
    half = 2 ** (ch - 1)
    if n <= half:
        if left:
            ans += 1
            left = False
            continue
        else:
            ans += half * 2
            left = False
            continue
    elif left:
        ans += half * 2
        left = True
        n -= half
    else:
        ans += 1
        left = True
        n -= half
print(ans)

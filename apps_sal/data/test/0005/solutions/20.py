(n, pos, l, r) = [int(i) for i in input().split()]
ans = 0
if l == 1 and r == n:
    ans = 0
elif l == 1:
    ans = abs(r - pos) + 1
elif r == n:
    ans = abs(pos - l) + 1
else:
    ans = r - l + 2
    if pos < l:
        ans += l - pos
    elif l <= pos and pos <= r:
        if abs(pos - l) < abs(r - pos):
            ans += pos - l
        else:
            ans += r - pos
    else:
        ans += pos - r
print(ans)

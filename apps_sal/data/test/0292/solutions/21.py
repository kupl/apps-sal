(h, n) = [int(_) for _ in input().split()]
start = 1
end = 2 ** h
last = 'l'
ans = 0
for i in range(h):
    mid = (start + end) // 2
    if n <= mid:
        end = mid
        if last == 'l':
            last = 'r'
            ans += 1
        else:
            ans += 2 ** (h - i)
    else:
        start = mid
        if last == 'r':
            last = 'l'
            ans += 1
        else:
            ans += 2 ** (h - i)
print(ans)

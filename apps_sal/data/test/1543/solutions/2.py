n = int(input())
last_r = None
last_b = None
last_p = None
ans = 0
max_r = 0
max_b = 0
max_p = 0
for _ in range(n):
    s = input().split()
    x = int(s[0])
    c = s[1]
    if c == 'B':
        if last_b != None:
            ans += x - last_b
            max_b = max(max_b, x - last_b)
        last_b = x
    if c == 'R':
        if last_r != None:
            ans += x - last_r
            max_r = max(max_r, x - last_r)
        last_r = x
    if c == 'P':
        if last_b != None:
            ans += x - last_b
            max_b = max(max_b, x - last_b)
        last_b = x
        if last_r != None:
            ans += x - last_r
            max_r = max(max_r, x - last_r)
        last_r = x
        if last_p != None:
            new_ans = (x - last_p) * 3
            new_ans -= max_r
            new_ans -= max_b
            if new_ans < (x - last_p) * 2:
                ans -= (x - last_p) * 2 - new_ans
        last_p = x
        max_b = 0
        max_r = 0
print(ans)

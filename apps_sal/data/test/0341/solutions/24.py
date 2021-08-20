(n, k) = map(int, input().split())
(r, s, p) = map(int, input().split())
t = input()
me = ''
ans = 0
for i in range(n):
    if t[i] == 'r':
        if i < k:
            me += 'p'
            ans += p
        elif me[i - k] != 'p':
            me += 'p'
            ans += p
        elif t[i - k] == 'p':
            me += 'p'
            ans += p
        else:
            me += 'r'
    elif t[i] == 's':
        if i < k:
            me += 'r'
            ans += r
        elif me[i - k] != 'r':
            me += 'r'
            ans += r
        elif t[i - k] == 'r':
            me += 'r'
            ans += r
        else:
            me += 's'
    elif i < k:
        me += 's'
        ans += s
    elif me[i - k] != 's':
        me += 's'
        ans += s
    elif t[i - k] == 's':
        me += 's'
        ans += s
    else:
        me += 'p'
print(ans)

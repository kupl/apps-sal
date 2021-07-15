m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
wd = ['monday', 'tuesday', 'wednesday', "thursday", "friday", "saturday", "sunday"]
a, b = [wd.index(input()) for i in range(2)]
for i in range(7):
    cur = i
    for j in range(11):
        nxt = (cur + m[j]) % 7
        if cur == a and nxt == b:
            print('YES')
            return
        cur = nxt
print('NO')

a = int(input())
cur = 1
last = 1
ans = 0
prev = []
while a > 0:
    a -= 1
    st = input()
    if st[2] == 'r':
        b = st.split(' ')
        b = int(b[1])
        if cur >= 2 ** 64:
            b = 1
        cur *= b
        prev.append(b)
    if st[2] == 'd' and st[1] == 'd':
        ans += cur
    if st[2] == 'd' and st[1] == 'n':
        val = prev[len(prev) - 1]
        prev.pop()
        cur /= val
    if ans >= 2 ** 32:
        break
if ans >= 2 ** 32:
    print('OVERFLOW!!!')
else:
    print(int(ans))

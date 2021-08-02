n = int(input())
t = input()
s = '110'

if t == '0':
    print((10**10))
    return
elif t == '1':
    print((2 * 10**10))
    return

res = 0
for i in range(3):
    a = (n + i + 2) // 3
    add = 10**10 - a + 1
    ok = True
    for j in range(n):
        if t[j] != s[(i + j) % 3]:
            ok = False
    if ok:
        res += add
print(res)

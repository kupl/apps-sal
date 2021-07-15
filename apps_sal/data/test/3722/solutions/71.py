mod = 10**9 + 7

def tr(c):
    if c == 'A':
        return 'B'
    else:
        return 'A'

n = int(input())
if n <= 3:
    print((1))
    return
caa = input()
cab = input()
cba = input()
cbb = input()
if cab == 'B':
    caa, cbb = cbb, caa
    caa = tr(caa)
    cab = tr(cab)
    cba = tr(cba)
    cbb = tr(cbb)
if caa == 'A':
    print((1))
    return
if cba == 'B':
    print((pow(2, n - 3, mod)))
    return
ans, prev = 2, 1
for i in range(4, n):
    ans, prev = (ans + prev) % mod, ans
print(ans)


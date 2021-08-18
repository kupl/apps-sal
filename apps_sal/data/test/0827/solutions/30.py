n = int(input())
t = input()

s = "110" * 100000
sz = (10**10) * 3


st = -1
ed = -1
for i in range(3):
    if s[i:i + len(t)] == t:
        st = i
        ed = i + len(t) - 1
        break

if t == '1':
    print(2 * (10 ** 10))
elif t == '0':
    print(10 ** 10)
elif st == -1:
    print(0)
else:
    a = st + 1
    d = 3
    l = 1
    r = 10**11
    m = -1
    ans = 0
    while l <= r:
        m = (l + r) // 2
        st = a + (m - 1) * d
        if st + len(t) - 1 > sz:
            r = m - 1
        else:
            ans = m
            l = m + 1
    print(ans)

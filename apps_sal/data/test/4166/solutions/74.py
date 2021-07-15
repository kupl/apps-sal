n, m = map(int, input().split())
sl = list(list(map(int, input().split())) for _ in range(m))

if n == 1:
    st, en = 10**(n-1)-1, 10**n
else:
    st, en = 10**(n-1), 10**n

flg = True
cnt = 0
for i in range(st, en):
    for s in sl:
        flg = True
        if str(i)[s[0]-1] == str(s[1]):
            continue
        else:
            flg = False
            break
    if flg:
        print(i)
        return
else:
    print(-1)

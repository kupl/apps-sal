
n, m = list(map(int, input().split()))
l = [0] * n
flg = [0] * n

for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    if flg[a] == 0 or (flg[a] == 1 and l[a] == b):
        l[a] = b
        flg[a] = 1
    else:
        print("-1")
        return

if n == 1 and flg[0] == 0:
    print((0))
    return
elif n > 1 and flg[0] == 0 and l[0] == 0:
    l[0] = 1
elif n > 1 and l[0] == 0:
    print("-1")
    return

ans = "".join(list(map(str, l)))
print(ans)



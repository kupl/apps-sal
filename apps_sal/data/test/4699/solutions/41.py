n, k = map(int, input().split())
d = list(input().split())
flg = True
while flg:
    flg = False
    m = list(str(n))
    for i in m:
        if i in d:
            flg = True
            break
    if flg:
        n += 1
print(n)

m = int(input())
if 1000 < m:
    if m % 1000 == 0:
        print(0)
    else:
        mai = m // 1000
        ryo = (mai + 1) * 1000
        print(ryo - m)
else:
    print(1000 - m)

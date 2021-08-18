n, m = map(int, input().split())
SC = [list(map(int, input().split())) for i in range(m)]
if n == 1:
    for i in range(10):
        for sc in SC:
            if str(i)[sc[0] - 1] != str(sc[1]):
                break
        else:
            print(i)
            return
    else:
        print(-1)
else:
    for i in range(10**(n - 1), 10**(n)):
        for sc in SC:
            if str(i)[sc[0] - 1] != str(sc[1]):
                break
        else:
            print(i)
            return
    else:
        print(-1)

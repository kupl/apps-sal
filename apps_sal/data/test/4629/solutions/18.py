q = int(input())
while q:
    q -= 1
    n = int(input())
    good = [1]
    x = 1
    while 1:
        t = 3 ** x
        ans = []
        for i in good:
            ans.append(t + i)
        good.append(t)
        for i in ans: good.append(i)
        x += 1
        if max(good) >= n: break
    for i in good:
        if i >= n:
            print(i)
            break

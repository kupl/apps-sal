n, t = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
s0 = 0
b = sorted(a, reverse=True)
big = b[0]
s = []
s0 = sum(b)
for i in b:
    s.append(s0)
    s0 -= i

money = t
ans = 0
for i, total in enumerate(s):
    big1 = b[i]
    if(money >= total):
        ans += ((n - i) * (money // total))
        money -= total * (money // total)
    if(money < big1):
        continue
    else:
        while(money >= big1):
            f1 = True
            for ls in range(n):
                if(money - a[ls] >= 0):
                    money -= a[ls]
                    f1 = False
                    ans += 1
                else:
                    pass
                ls += 1
            if(f1 == True):
                break
        if(f1 == True):
            break


print(ans)

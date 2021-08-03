n = int(input())
a = list(map(int, input().split()))

d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
d = sorted(d.items(), key=lambda x: x[0], reverse=True)

m = len(d)
ans = 0
flg = True
for i in range(m):
    k, v = d[i][0], d[i][1]
    if ans == 0:
        if v >= 4:
            ans = k**2
            flg = True
            break
        elif v >= 2:
            ans = k
    elif v >= 2:
        ans *= k
        flg = True
        break
print(ans) if flg else print(0)

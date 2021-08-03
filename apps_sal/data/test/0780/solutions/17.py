s = input()
mp = [0] * 10
for i in range(1, len(s)):
    x = (int(s[i]) - int(s[i - 1]) + 10) % 10
    mp[x] += 1


def tab(a, b):
    tb = [1000] * 10
    for i in range(10):
        for j in range(10):
            if i == 0 and j == 0:
                continue
            x = (a * i + b * j) % 10
            tb[x] = min(tb[x], i + j)
    return tb


for x in range(10):
    for y in range(10):
        tb = tab(x, y)
        flg = True
        for i in range(10):
            if mp[i] > 0 and tb[i] == 1000:
                flg = False
                break
        if flg == False:
            print(-1, end=' ')
            continue

        tb = tab(x, y)
        ans = 0
        for t in range(10):
            ans += mp[t] * (tb[t] - 1)
        print(ans, end=' ')
    print()

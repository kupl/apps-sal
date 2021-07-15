def sm(x) :
    return x * (x + 1) // 2

def get_sum(l, r) :
    return sm(r) - sm(l - 1)

n, x = list(map(int, input().split()))
d = [int(i) for i in input().split()]
d = d[:] + d[:]
n *= 2
pre = [d[0]]
month, day, days, tot = n - 1, d[n - 1] + 1, 0, 0
ans = 0
for i in range(n - 1, -1, -1) :
    while days < x and month >= 0:
        if day > 1 :
            cnt = min(x - days, day - 1)
            tot += get_sum(day - cnt, day - 1)
            days += cnt
            day -= cnt
        else :
            month -= 1
            day = d[month] + 1
    ans = max(ans, tot)
    tot -= get_sum(1, d[i])
    days -= d[i]
print(ans)



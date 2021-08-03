def lucky(x):
    return (x % 10 == 7)


x = int(input())
h, m = list(map(int, input().split()))
t = 60 * h + m

ans = float('inf')
for hh in range(24):
    for mm in range(60):
        if lucky(hh) or lucky(mm):
            s = 60 * hh + mm
            while t < s:
                s -= 60 * 24

            r = t - s
            if r % x != 0:
                continue

            ans = min(ans, r // x)

print(ans)

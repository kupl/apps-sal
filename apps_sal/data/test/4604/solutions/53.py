n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
d = [0] * (n + 1)
for x in a:
    d[x] += 1
ans = 1
if n % 2 == 0:
    sw = 1
    for (i, x) in enumerate(d):
        if i % 2 != 0:
            if x == 2:
                ans *= 2
                ans %= mod
            else:
                sw = 0
                break
        elif x != 0:
            sw = 0
            break
else:
    sw = 1
    for (i, x) in enumerate(d):
        if i % 2 == 0:
            if i == 0:
                if x != 1:
                    sw = 0
                    break
            elif x == 2:
                ans *= 2
                ans %= mod
            else:
                sw = 0
                break
        elif x != 0:
            sw = 0
            break
if sw == 0:
    ans = 0
print(ans)

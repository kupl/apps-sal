s, x = list(map(int, input().split()))
rem = int(s == x) * 2
p, t, cur = [], 0, 1
for i in range(64):
    if x % 2:
        t += 1
        s -= cur
    else:
        p.append(cur * 2)
    cur *= 2
    x //= 2
for i in p[::-1]:
    if s >= i:
        s -= i
ans = 0 if s else 2 ** t - rem
print(ans)

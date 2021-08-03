def read(): return list(map(int, input().split()))


a1, a2 = read()
if a1 <= 1 and a2 <= 1:
    ans = 0
else:
    ans = 0
    cur = 0
    while a1 > 0 and a2 > 0:
        cur = 1 if a1 < a2 else 2
        if cur == 0:
            a1 -= 2
            a2 -= 2
        elif cur == 1:
            a1 += 1
            a2 -= 2
        elif cur == 2:
            a1 -= 2
            a2 += 1
        ans += 1

print(ans)

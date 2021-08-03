t = int(input())
ans_l = []
for _ in range(t):
    n = int(input())
    ans = 0
    ans += 9 * (len(str(n)) - 1)
    for i in range(1, 10):
        x = int(str(i) * len(str(n)))
        if x <= n:
            ans += 1
        else:
            break
    ans_l.append(ans)
print(*ans_l, sep='\n')

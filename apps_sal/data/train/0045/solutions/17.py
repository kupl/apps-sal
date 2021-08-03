gans = []
for _ in range(int(input())):
    n = int(input())
    ans = 0
    cur = 1
    while n >= cur * (cur + 1) // 2:
        n -= cur * (cur + 1) // 2
        ans += 1
        cur = cur * 2 + 1
        #print(cur, n)
    gans.append(ans)
print('\n'.join(map(str, gans)))

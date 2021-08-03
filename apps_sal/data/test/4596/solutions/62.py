def getints(): return map(int, input().split())


n = int(input())
a = list(getints())
ans = 10 ** 9
for x in a:
    cnt = 0
    while x % 2 == 0:
        x /= 2
        cnt += 1
    ans = min(ans, cnt)
print(ans)

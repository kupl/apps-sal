n, m = map(int, input().split())
s = input()
s = s[::-1]
ans = []
cur = 0
c = 0
# while cur < n and c < 100:
while cur < n:
    d = n - cur
    r = min(m, d)
    cnt = 0
    for i in range(r):
        x = r - i
        if s[cur + x] == '0':
            ans.append(x)
            cur += x
            # print(x)
            break
        else:
            cnt += 1
    if cnt == r:
        print(-1)
        return
    #c += 1
    # print(cur,r)


print(*ans[::-1])

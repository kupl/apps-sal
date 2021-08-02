# 146_F
n, m = map(int, input().split())
s = input()[::-1]
ans = []

flg = True
cur = 0
while cur < n and flg:
    for to in range(cur + m, cur, -1):
        if to > n:
            continue

        if s[to] == '0':
            ans.append(to - cur)
            cur = to
            break

        if to == cur + 1:
            flg = False

if flg:
    print(*ans[::-1])
else:
    print(-1)

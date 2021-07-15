s, c = map(int,input().split())

cnt = 0
if 2*s <= c:
    cnt += s
    c -= 2*s
else:
    cnt += c // 2
    c = 0

cnt += c//4
print(cnt)

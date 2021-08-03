l, r, k = map(int, input().split())

s = 1

while s < l:
    s *= k

ans = []
while s <= r:
    ans.append(s)
    s *= k

if ans:
    print(' '.join(str(v) for v in ans))
else:
    print(-1)

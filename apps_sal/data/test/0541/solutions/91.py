n,m = list(map(int,input().split()))
l = sorted(list( list(map(int,input().split())) for _ in range(m)), key=lambda x: x[1])
br = -1
ans = 0
for i in l:
    head, tail = i[0], i[1]
    if head < br:
        continue
    else:
        br = tail
        ans += 1
print(ans)


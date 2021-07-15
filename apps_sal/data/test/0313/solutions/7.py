input()
pprev, prev = None, None
ans = 0
for i in input().split():
    if i == '1':
        ans += 1
        if prev == '0' and pprev == '1':
            ans += 1
    pprev, prev = prev, i
print(ans)


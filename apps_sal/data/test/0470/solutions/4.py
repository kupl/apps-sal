l = list(map(int, input().split()))
orig = sum(l)
ans = sum(l)
for i in l:
    if l.count(i) == 2:
        ans = min(ans, orig-i*2)
    elif l.count(i) >= 3:
        ans = min(ans, orig-i*3)
print(ans)


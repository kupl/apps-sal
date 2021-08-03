n, h = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for x in a:
    if x > h:
        ans += 2
    else:
        ans += 1
print(ans)

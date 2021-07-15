n, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
ans = 0
for i in range(x):
    if not i in a:
        ans += 1
if x in a:
    ans += 1
print(ans)

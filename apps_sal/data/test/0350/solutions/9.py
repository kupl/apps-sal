n = int(input())
l = list(map(int, input().split()))
l.sort(reverse = True)
check = set()
ans = 0
for i in l:
    x = i
    while x in check:
        x -= 1
    if x < 0:
        continue
    ans += x
    check.add(x)
print(ans)

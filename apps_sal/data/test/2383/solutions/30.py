a = int(input())
b = list(map(int, input().split()))
c = 1
ans = 0
for i in b:
    if i == c:
        c += 1
    else:
        ans += 1
if ans == a:
    ans = -1
print(ans)

n = int(input())
l = list(map(int, input().split()))
ans = 0
x = 1
for i in l:
    if i == x:
        x += 1
    else:
        ans += 1

if ans == len(l):
    print((-1))
else:
    print(ans)

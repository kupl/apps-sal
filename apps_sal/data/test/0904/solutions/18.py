n = int(input())
a = input().split()
ans = 0
for i in a:
    cnt = 0
    for e in i:
        if e in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            cnt += 1
    ans = max(ans, cnt)
print(ans)

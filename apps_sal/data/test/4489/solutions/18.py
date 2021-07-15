n = int(input())
blue = list()
for i in range(n):
    blue.append(input())
m = int(input())
red = list()
for j in range(m):
    red.append(input())
ans = 0
for p in range(n):
    cnt = 0
    for q in range(n):
        if blue[p] == blue[q]:
            cnt += 1
    for r in range(m):
        if blue[p] == red[r]:
            cnt -= 1
    ans = max(ans, cnt)
print(ans)

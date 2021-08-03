n = int(input())
lst = [int(x) for x in input().split()]
cur, cnt = 0, 0
for i in lst:
    if i == cur:
        cnt += 1
    elif cnt == 0:
        cur, cnt = i, 1
    else:
        cnt -= 1
cnt = 0
for i in lst:
    if i == cur:
        cnt += 1
print("YES" if cnt + (cnt - 1) <= n else "NO")

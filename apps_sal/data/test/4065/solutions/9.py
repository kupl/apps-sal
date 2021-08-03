n = int(input())
s = input().split()
l = [int(s[i]) for i in range(n)]

res = 1
cnt = 1
now = l[0]
for i in range(1, n):
    if now * 2 >= l[i]:
        now = l[i]
        cnt += 1
    else:
        now = l[i]
        res = max(res, cnt)
        cnt = 1
res = max(res, cnt)
print(res)

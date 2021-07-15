n, x = map(int, input().split())
cur1=cur2=cur=res=0
for a in map(int, input().split()):
    cur1 = max(cur1 + a, 0)
    cur2 = max(cur2 + a * x, cur1)
    cur = max(cur + a, cur2)
    res = max(res, cur)
print(res)

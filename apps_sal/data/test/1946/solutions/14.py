d = {}

n = int(input())
for i in range(n):
    num, pro = map(int, input().split())
    try:
        d[num] = max(d[num], pro)
    except:
        d[num] = pro
m = int(input())
for i in range(m):
    num, pro = map(int, input().split())
    try:
        d[num] = max(d[num], pro)
    except:
        d[num] = pro
ans = 0
for ele in d:
    ans += d[ele]
print(ans)

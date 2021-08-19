n, m = list(map(int, input().split()))
p = []
for _ in range(m):
    a, b = list(map(int, input().split()))
    p.append([a, b])
# print(p)
p.sort(key=lambda x: x[1])
# print(p)
ans = 0
cur = 0
for i in range(m):
    if cur <= p[i][0]:
        #print("i:%d残す,cur:%d,p[i][1]:%d,p[i][0]:%d" % (i,cur,p[i][1],p[i][0]))
        ans += 1
        cur = p[i][1]
print(ans)

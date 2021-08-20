N = int(input())
l = []
for i in range(N):
    v = int(input())
    l.append(v)
v = l[0]
ans = 1
while v != 2 and v != -1:
    tmp = l[v - 1]
    l[v - 1] = -1
    v = tmp
    ans += 1
if v == 2:
    print(ans)
else:
    print(-1)

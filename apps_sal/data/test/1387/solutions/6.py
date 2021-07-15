n,t = list(map(int, input().split()))
l = input().split()
for i in range(n-1):
    l[i] = int(l[i])
l = [0]+l
now = 1
while 1:
    now += l[now]
    if now > t:
        ans = 0
        break
    if now == t:
        ans = 1
        break

if ans == 0:
    print("NO")
else:
    print("YES")


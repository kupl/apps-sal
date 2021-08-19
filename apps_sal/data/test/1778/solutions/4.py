# Problem C: Gambling

n = int(input())

a = input().split()
b = input().split()

for i in range(n):
    a[i] = int(a[i])
    b[i] = int(b[i])


goList = []
for i in range(n):
    cur = (a[i], 1)
    goList.append(cur)
for i in range(n):
    cur = (b[i], 2)
    goList.append(cur)

goList.sort(reverse=True)

ans = 0

for i in range(2 * n):
    cur = goList[i]
    pts = cur[0]
    owner = cur[1]
    if(i % 2 == 0):  # First Player
        if(owner == 1):
            ans += pts
    else:
        if(owner == 2):
            ans -= pts

print(ans)

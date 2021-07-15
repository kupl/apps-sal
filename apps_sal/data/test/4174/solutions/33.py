n, x = map(int, input().split())
l = list(map(int, input().split()))
xlist = [0]
num = 0
for i in l:
    num += i
    xlist.append(num)
cnt = 0
for j in xlist:
    if j <= x:
        cnt += 1
print(cnt)

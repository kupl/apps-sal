n,m = map(int,input().split())
s = input()[::-1]

#まず何手でクリアできるかを把握する
count = 1
inf = 10**10

#ゴールまでその地点から何手で到達できるかを記録する
length = [inf]*(n+1)
length[0] = 0
now = 0
flag = True

while flag:
    ok = 0
    for i in range(1,m+1):
        if s[now+i] == "1":
            continue
        length[now+i] = count
        ok = now+i
        if now+i == n:
            flag = False
            break
    if ok == 0:
        print(-1)
        return
    now = ok
    count += 1

count -= 2

#スタートからの軌跡を格納するリスト
li = []
length = length[::-1]
point = 0

for i,j in enumerate(length):
    if j == count:
        count -= 1
        li.append(point)
        point = 0
    point += 1

print(*li)

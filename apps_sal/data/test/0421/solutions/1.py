def snd(lst):
    return lst[1]
n = int(input())
l = []
for i in range(0, n):
    l.append([int(i) for i in input().split()])
l.sort(key=snd)
e = 0
ans = 0
for p in l:
    if (p[0] > e):
        ans+=1
        e = p[1]
print(ans)


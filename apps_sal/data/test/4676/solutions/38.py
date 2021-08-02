#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
o = list(input())
e = list(input())
oc = 0
ec = 0

ans = ''

n = len(o) + len(e)
for i in range(1, n + 1):
    if i % 2 == 0:
        add = e[ec]
        ec += 1
    else:
        add = o[oc]
        oc += 1
    ans += add

print(ans)

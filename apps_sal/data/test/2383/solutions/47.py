N = int(input())
li = list(map(int, input().split()))
li_com = [i+1 for i in range(N)]
an = 0
com = 0
for i in range(N):
    if li_com[com] == li[i]:
        com += 1
    else:
        an += 1

if com == 0:
    print(-1)
else:
    print(an)

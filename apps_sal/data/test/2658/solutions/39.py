n, k = list(map(int, input().split()))
button = list(map(int, input().split()))
visit = [-1] * n
hisitory = [-1]
push = 0
f = 0

for i in range(k):
    visit[push] = i + 1
    hisitory.append(push)
    push = button[push] - 1
    if(visit[push] != -1):
        f = 1
        start = visit[push]
        last = push
        end = i + 1
        break
if(f == 0):
    print((button[hisitory[-1]]))
else:
    geta = start - 1
    loopk = k - geta
    loop = end - start + 1
    modk = loopk % loop
    if(modk == 0):
        modk = loop
    print((button[hisitory[geta + modk]]))
    # print(hisitory)
    # print(geta,modk,loop)

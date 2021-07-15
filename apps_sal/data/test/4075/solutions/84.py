#m = int(input())
n, m = list(map(int, input().split()))
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]
switch = []
kl = []
for i in range(m):
    temp = list(map(int, input().split()))
    kl.append(temp[0])
    switch.append(temp[1:])
pl = list(map(int, input().split()))
# print(switch)

pattern = [[0 for _ in range(n)] for _1 in range(2**n)]
for i in range(2**n):
    for j in range(n):
        if ((i >> j) & 1):  # 二進数iの下から数えてj桁目が1か否か
            pattern[i][j] = 1

ans = 0
for ptnum, spt in enumerate(pattern):
    islit = True
    for lightnum in range(m):
        count = 0
        for s in switch[lightnum]:
            if spt[s-1] == 1:
                count += 1
        if count % 2 != pl[lightnum]:
            islit = False
            break
    if islit:
        ans += 1
print(ans)


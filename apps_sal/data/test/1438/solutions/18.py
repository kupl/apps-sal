n, magic = list(map(int, input().split()))
gramNeed = list(map(int, input().split()))
gramHas = list(map(int, input().split()))

able = []
remain = []
for i in range(n):
    able.append([gramHas[i] // gramNeed[i], gramHas[i] % gramNeed[i], gramNeed[i]])
able.sort(key = lambda x: x[0])
ans = able[0][0]
for i in range(n):
    able[i][0] -= ans
while magic > 0:
    i = 0
    for i in range(n):
        if able[i][0] == 0:
            able[i][1] += 1
            magic -= 1
            if able[i][1] == able[i][2]:
                able[i][0] += 1
                able[i][1] = 0
            break
    if min(able, key = lambda x: x[0])[0] != 0:
        ans += 1
        for i in range(n):
            able[i][0] -= 1
print(ans)




"""
magic = 1
need =   2 1 4
has =   11 3 16
able =   2 0 1
remain = 1 0 0

ans = 3

magic = 3
need =   4 3  5  6
has =   11 15 14 20
able =   0 3  0  1
remain = 3 0  4  2
lack  =  1 3  1  4

ans = 2
"""


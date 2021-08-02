import math
n = int(input())
ass = n * 2
v = [int(i) for i in input().split()]
ans = [[0 for i in range(20)] for i in range(n)]
ch = [[0 for i in range(20)] for i in range(n)]
for i in range(n):
    ch[i][0] = v[i]
kol = 1
j = 2
while(kol < 20):
    i = 0
    while(i + j - 1 + ass < n + ass):
        shize = i + j - 1
        ch[i][kol] = (ch[i][kol - 1] + ch[int((i + shize + 1) / 2)][kol - 1]) % 10
        pl = 0
        if((ch[i][kol - 1] + ch[int((i + shize + 1) / 2)][kol - 1]) >= 10):
            pl = 1
        ans[i][kol] = ans[i][kol - 1] + ans[int((i + shize + 1) / 2)][kol - 1] + pl

        i += 1

    j *= 2
    kol += 1
q = int(input())
for i in range(q):
    a, b = [int(i) for i in input().split()]
    a -= 1 + ass - ass
    b -= 1 - ass + ass
    kol = int(math.log2(b - a + 1))
    print(ans[a][kol])

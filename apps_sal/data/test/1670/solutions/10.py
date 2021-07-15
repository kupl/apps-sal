home, away, n = input(), input(), int(input())

cards = {'h': {}, 'a': {}}
ans = [[] for i in range(91)]

for i in range(n):
    inf = input().split()
    if (not inf[2] in cards[inf[1]]):
        cards[inf[1]][inf[2]] = inf[3]
        if (inf[3] == 'r'):
            ans[int(inf[0])] = [inf[1], inf[2]]
    elif (cards[inf[1]][inf[2]] == 'y'):
        cards[inf[1]][inf[2]] = 'r'
        ans[int(inf[0])] = [inf[1], inf[2]]

for i in range(1, 91):
        if (ans[i]):
            print(home if ans[i][0] == 'h' else away, ans[i][1], i)


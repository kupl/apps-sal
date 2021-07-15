import itertools as it

n, m = list(map(int, input().split()))
a = list(list(map(int, input().split())) for _ in range(m))

#print(a)

#無向グラフのルート作成（リスト）
for i in range(len(a)):
    a.append([a[i][1],a[i][0]])
#print(a)


#１を始点とするルートを全探索で作成
lis  = list(it.permutations(list(range(2, n + 1))))
#print(lis)
for i in range(len(lis)):
    lis[i] = (1,) + lis[i]
#print(lis)

#リストに変換
lis2 = []
for i in range(len(lis)):
    lis[i] = list(lis[i])
    lis2.append(lis[i])
#print(lis2)

#ルート探索
#lis3 = []
ans = 0
for i in range(len(lis2)):
    check = True
    for j in range(len(lis2[i]) - 1):
        if lis2[i][j : j + 2] not in a:
            check = False
    if check:
        ans += 1
print(ans)


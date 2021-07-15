n, m = [int(x) for x in input().split()]
slova = []
for i in range(n):
    slova.append(input())
na_zmazanie = [int(x)-1 for x in input().split()]

dlzka_zmazanych = len(slova[na_zmazanie[0]])
for i in na_zmazanie:
    if len(slova[i]) != dlzka_zmazanych:
        print("No")
        return

zmaz = [False] * n
for i in na_zmazanie:
    zmaz[i] = True
matchujuce_nie_na_zmazanie = [i for i in range(n) if zmaz[i] == False and len(slova[i]) == dlzka_zmazanych] 

pattern = ""
for i in range(0, dlzka_zmazanych):
    znak_prveho = slova[na_zmazanie[0]][i]
    for x in na_zmazanie:
        if slova[x][i] != znak_prveho:
            pattern += "?"
            break
    else:
        pattern += znak_prveho
        nove_matchujuce = []
        for y in matchujuce_nie_na_zmazanie:
            if slova[y][i] == znak_prveho: 
                nove_matchujuce.append(y)
        matchujuce_nie_na_zmazanie = nove_matchujuce

if len(matchujuce_nie_na_zmazanie) == 0:
    print("Yes")
    print(pattern)
else:
    print("No")


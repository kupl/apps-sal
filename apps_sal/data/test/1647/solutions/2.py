n = int(input())
S = set()
Slovar = []
sviter = input()
futbol = input()
res = 0
Ans = []
for i in range(n):
    if sviter[i] != futbol[i]:
        if sviter[i] not in S and futbol[i] not in S:
            Slovar.append(sviter[i] + futbol[i])
            S.add(sviter[i])
            S.add(futbol[i])
            res += 1
            Ans.append([sviter[i], futbol[i]])
        elif sviter[i] in S and futbol[i] not in S:
            S.add(futbol[i])
            for j in range(len(Slovar)):
                if sviter[i] in Slovar[j]:
                    Slovar[j] += futbol[i]
                    res += 1
                    Ans.append([sviter[i], futbol[i]])                    
                    break
        elif sviter[i] not in S and futbol[i] in S:
            S.add(sviter[i])
            for j in range(len(Slovar)):
                if futbol[i] in Slovar[j]:
                    Slovar[j] += sviter[i]
                    res += 1
                    Ans.append([sviter[i], futbol[i]])                     
                    break
        elif sviter[i] in S and futbol[i] in S:
            for j in range(len(Slovar)):
                if futbol[i] in Slovar[j]:
                    a = j
                if sviter[i] in Slovar[j]:
                    b = j                
            if a != b:
                Slovar[a] = Slovar[a] + Slovar[b]
                Slovar[b] = ''
                res += 1
                Ans.append([sviter[i], futbol[i]])
        #print(i, res, Slovar, S)
print(res)
for i in range(res):
    print(*Ans[i])

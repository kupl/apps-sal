n = int(input())
ar = list(map(int, input().split()))
dic = {}
ar.reverse()
nar = []
for x in ar:
    if dic.get(x) is None:
        nar.append(x)
        dic[x] = True
nar.reverse()
print(len(nar))
print(*nar)

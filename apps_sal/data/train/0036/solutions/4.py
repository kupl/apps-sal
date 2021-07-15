num = int(input())
piles = list(map(int, input().split(' ')))
tuplex = []
curr = 1
for i in piles:
    tuplex.append((curr, curr+i-1))
    curr = curr+i

quer = int(input())
queries = list(map(int, input().split(' ')))
quer2 = [[queries[x], x, -1] for x in range(len(queries))]
quer2.sort(key = lambda x:x[0])

ind = 0
for i in range(len(quer2)):
    while not (tuplex[ind][0] <= quer2[i][0] <= tuplex[ind][1]):
        ind += 1
    quer2[i][2] = ind

quer2.sort(key = lambda x:x[1])
for i in quer2:
    print(i[2]+1)

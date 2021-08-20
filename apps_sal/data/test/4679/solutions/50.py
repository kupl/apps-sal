G = {}
l = ['a', 'b', 'c']
for i in l:
    G[i] = list(input())
s = l[0]
while True:
    if len(G[s]) == 0:
        print(s.upper())
        break
    s = G[s].pop(0)

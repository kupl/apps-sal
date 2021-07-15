import operator

n = int(input())
points = list(map(int, input().split()))

def praf(g):
    for i in g[1:]:
        print(''.join(i))

def calc(n):
    nonlocal points
    a = b = 0
    step = 1
    for i in range(n):
        a += points[i]
        b += points[i] * step
        step = -step
    return (a, b)

seq = [(0, 0)]
for i in range(len(points)):
    seq.append(calc(i+1))

seq = sorted(seq, key=lambda x: x[0])
seq = {i: seq[i] for i in range(len(seq))}
#print(seq)

for i in range(len(seq)):
    r = 0
    if i != len(seq)-1:
        if seq[i][1] > seq[i+1][1]:
            r = -1
        else:
            r = 1

    seq[i] = seq[i] + tuple([r])


seqy = sorted(list(seq.items()), key=lambda x: x[1][1], reverse=True)

pts = {x[0]: x[2] for x in list(seq.values())}

pts[seq[len(seq)-1][0]] = 1

#print('---seq---')
#print(seq)
#print('----seqy---')
#print(seqy)
#print('---pts---')
#print(pts)

graph = [[' '] * seq[len(seq)-1][0] for x in range(seqy[0][1][1]-seqy[-1][1][1]+1)]

y = seqy[0][1][1]


way = pts[0]
for i in range(len(graph[0])):
    if i in list(pts.keys()):
        if pts[i] != way:
            if way == 1:
                y+=1
            else:
                y-=1

        way = pts[i]


    graph[y][i] = '/' if way == 1 else '\\'
    y -= way
#    praf(graph)


#print('----------------graph-----------------------------------------------------------')
praf(graph)







#praf(graph)



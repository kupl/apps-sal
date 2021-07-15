import sys
 
# inf = open('input.txt', 'r')
# reader = (line.rstrip() for line in inf)
reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__
 
t = int(input())
for _ in range(t):
    n = int(input())
    edges = []
    for i in range(n):
        li, ri = list(map(int, input().split()))
        edges.append((li, 0, i))
        edges.append((ri, 1, i))
    edges.sort()
    ctr = [0] * n
    opened = set()
    segmCtr = 0
    for k, (e, isEnd, i) in enumerate(edges):
        if isEnd:
            opened.remove(i)
            if not opened and edges[k-1][2] == i:
                ctr[i] -= 1
            elif len(opened) == 1 and edges[k+1][1] == 0:
                for j in opened:
                    ctr[j] += 1
        else:
            if not opened:
                segmCtr += 1
            opened.add(i)
    print(segmCtr + max(ctr))

# inf.close()


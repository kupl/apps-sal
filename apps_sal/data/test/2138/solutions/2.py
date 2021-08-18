def readline(): return list(map(int, input().split()))


def SolveDegreeSet(DegreSet, n):
    edges = []
    verticesCount = 0
    if(n == 0):
        verticesCount = 1
        return edges, verticesCount
    if(n == 1):
        verticesCount = DegreSet[0] + 1
        for i in range(1, verticesCount + 1):
            for j in range(i + 1, verticesCount + 1):
                edges.append([i, j])
        return edges, verticesCount

    newDegreeSet = []
    for i in range(1, n - 1):
        newDegreeSet.append(DegreSet[i] - DegreSet[0])
    prevSolveDegreeSet = SolveDegreeSet(newDegreeSet, n - 2)

    verticesCount = prevSolveDegreeSet[1]
    edges = prevSolveDegreeSet[0]

    verticesCount += (DegreSet[n - 1] - DegreSet[n - 2])
    for i in range(0, DegreSet[0]):
        verticesCount += 1
        for j in range(1, verticesCount):
            edges.append([j, verticesCount])
    return edges, verticesCount


n, = readline()
d = readline()

par = list(SolveDegreeSet(d, n))
edges = par[0]
print(len(edges))
print("\n".join(map("{0[0]} {0[1]}".format, edges)))

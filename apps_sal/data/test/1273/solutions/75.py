from collections import defaultdict
N = int(input())
edge = []
relation = defaultdict(set)
for i in range(N - 1):
    a, b = map(lambda x: x - 1, map(int, input().split()))
    edge.append((a, b))
    relation[a].add(b)
    relation[b].add(a)

print(max(map(lambda x: len(relation[x]), relation)))
answer = {}
queue = []
queue.append((0, 0))
already = set()
counter = 0
already.add(0)
while counter < len(queue):
    node, color = queue[counter]
    c = 1 if color != 1 else 2
    for n in relation[node]:
        if n not in already:
            queue.append((n, c))
            already.add(n)
            answer[(node, n)] = c
            c += 1
            if c == color:
                c += 1
    counter += 1
for e in edge:
    print(answer[e])

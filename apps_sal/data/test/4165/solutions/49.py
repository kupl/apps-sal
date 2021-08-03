num = int(input())
edges = list(map(int, input().split(' ')))
can_draw = 0
edges.sort(reverse=True)
if edges[0] < sum(edges[1:]):
    print("Yes")
else:
    print("No")

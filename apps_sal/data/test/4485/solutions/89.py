n, m = list(map(int, input().split()))
root_map = dict()
root_map[1] = set()
root_map[n] = set()

for i in range(m):
    a, b = list(map(int, input().split()))
    if a == 1 or a == n:
        root_map[a].add(b)
    if b == 1 or b == n:
        root_map[b].add(a)

for i in root_map[1]:
    if i in root_map[n]:
        print("POSSIBLE")
        break
else:
    print("IMPOSSIBLE")


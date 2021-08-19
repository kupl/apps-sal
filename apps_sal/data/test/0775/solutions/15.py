iters = int(input().split()[2])
holes = {int(x) for x in input().split()}
current = 1
for _ in range(iters):
    (src, dest) = (int(x) for x in input().split())
    if current in holes:
        break
    if current == src:
        current = dest
    elif current == dest:
        current = src
print(current)

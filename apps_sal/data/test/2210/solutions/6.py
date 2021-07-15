for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    neighbors = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        neighbors[u-1].append(v-1)
        neighbors[v-1].append(u-1)
    x-=1

    if len(neighbors[x]) < 2:
        print("Ayush")
        continue

    if n % 2 == 1:
        print("Ashish")
    else:
        print("Ayush")


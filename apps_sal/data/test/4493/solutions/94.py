N = 3
c = [list(map(int, input().split())) for _ in range(N)]
ds = [sum(c[j][(i + j) % 3] for j in range(N)) for i in range(N)]
if ds[0] == ds[1] == ds[2]:
    print("Yes")
else:
    print("No")

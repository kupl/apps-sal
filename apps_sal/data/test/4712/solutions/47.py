h, w = map(int, input().split())
grid = [["#"] * (w + 2) for _ in range(h + 2)]

for i in range(h):
    grid[i + 1] = ["#"] + list(map(str, input().rstrip())) + ["#"]

for i in range(h + 2):
    print("".join(grid[i]))

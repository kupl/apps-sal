n, m = map(int, input().split())
n -= 1
x = [[] for _ in range(200000)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    x[a].append(b)

cnt = 0
for i in x[0]:
    if n in x[i]:
        print("POSSIBLE")
        return
print("IMPOSSIBLE")

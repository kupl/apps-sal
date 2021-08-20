n = int(input())
ans = []
vert = set()
hor = set()
for i in range(n * n):
    (a, b) = map(int, input().split())
    if a not in vert and b not in hor:
        ans.append(i + 1)
        vert.add(a)
        hor.add(b)
print(*ans)

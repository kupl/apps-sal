n, m = map(int, input().split())
conditions = [tuple(map(int, input().split())) for j in range(m)]
exist = False
for i in range(1000):
    if len(str(i)) == n and all(str(i)[s - 1] == str(c) for s, c in conditions):
        ans = i
        exist = True
        break
print(ans if exist else -1)

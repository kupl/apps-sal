(n, d) = map(int, input().split())
pos = list(map(int, input().split()))
points = list(map(int, input().split()))
cur = d - 1
cur_score = pos[cur] + points[0]
q = n - 1
for i in range(cur):
    if pos[i] + points[q] <= cur_score:
        q -= 1
        cur -= 1
print(cur + 1)

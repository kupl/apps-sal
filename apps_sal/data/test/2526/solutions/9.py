(x, y, a, b, c) = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p = sorted(p, reverse=True)
q = sorted(q, reverse=True)
r = sorted(r)
box = []
ans = 0
for i in range(x):
    box.append(p[i])
for j in range(y):
    box.append(q[j])
box = box + r
box = sorted(box, reverse=True)
for k in range(x + y):
    ans += box[k]
print(ans)

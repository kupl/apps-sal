N, W = map(int, input().split())
w, v = [], []
for _ in range(N):
  wi, vi = map(int, input().split())
  w.append(wi)
  v.append(vi)

V = [[], [], [], []]
for wi, vi in zip(w, v):
  V[wi - w[0]].append(vi)

for vv in V:
  vv.sort(reverse=True)

ans = 0
for i in range(len(V[0]) + 1):
  for j in range(len(V[1]) + 1):
    for k in range(len(V[2]) + 1):
      for l in range(len(V[3]) + 1):
        if w[0] * i + (w[0] + 1)* j + (w[0]+2)*k + (w[0] + 3) * l <= W:
          ans = max(ans, sum(V[0][:i]) +sum(V[1][:j]) +sum(V[2][:k]) +sum(V[3][:l])) 
print(ans)

X, Y, A, B, C = map(int, input().split())
p = sorted(list(map(int, input().split())))[::-1]
q = sorted(list(map(int, input().split())))[::-1]
r = sorted(list(map(int, input().split())))[::-1]

i = X - 1
j = Y - 1
k = 0

p.append(float("INF"))
q.append(float("INF"))
r.append(-1)

while p[i] < r[k] or q[j] < r[k]:
    if p[i] < q[j]:
        i -= 1
        k += 1
    else:
        j -= 1
        k += 1

ans = 0
if i != -1:
    ans += sum(p[:i + 1])
if j != -1:
    ans += sum(q[:j + 1])
if k != 0:
    ans += sum(r[:k])

print(ans)

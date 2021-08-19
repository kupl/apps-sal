(n, p) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
m = max((a[i] - i for i in range(n)))
M = a[p - 1] - 1
ban = [0 for i in range(p)]
ans = []
query = [(a[i] - 1 - i, 1, -100) for i in range(n)]
for x in range(m, M + 1):
    query.append((x, 0, -100))
for i in range(n):
    query.append((a[i], -1, i))
query.sort()
for (val, q, id) in query:
    if q == -1:
        r = (val - id - 1) % p
        ban[r] -= 1
    elif q == 0:
        if ban[val % p] == 0:
            ans.append(val)
    else:
        ban[val % p] += 1
ans.sort()
print(len(ans))
print(*ans)

n, m = list(map(int, input().split()))
p = list(map(int, input().split()))
gr = [set() for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    gr[a].add(b)

cant = {p[-1] - 1}
for i in range(n - 2, -1, -1):
    cnt = 0
    for j in gr[p[i] - 1]:
        if j in cant:
            cnt += 1
    # print(p[i], gr[p[i] - 1], cnt)
    if cnt != len(cant):
        cant.add(p[i] - 1)
# print(cant)
print(n - len(cant))

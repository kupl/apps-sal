n = int(input())

c = list(map(int, input().split()))

a = list([int(x) - 1 for x in input().split()])

deg_in = [0 for _ in range(n)]

d_in_to_v_set = {i: set() for i in range(n + 1)}

for ai in a:
    deg_in[ai] += 1

for i in range(n):
    d_in_to_v_set[deg_in[i]].add(i)

while d_in_to_v_set[0] != set():
    l = list(d_in_to_v_set[0])
    for u in l:
        d_in_to_v_set[deg_in[a[u]]].remove(a[u])
        d_in_to_v_set[deg_in[a[u]] - 1].add(a[u])
        d_in_to_v_set[0].remove(u)
        deg_in[a[u]] -= 1

p = [0 for _ in range(n)]

for v in d_in_to_v_set[1]:
    p[v] = 1

ans, cur = 0, 10**5

for i in range(n):
    s = i
    cur = 10**5
    while p[s] != 0:
        cur = min(cur, c[s])
        p[s] = 0
        s = a[s]
    ans += cur if cur < 10**5 else 0

print(ans)

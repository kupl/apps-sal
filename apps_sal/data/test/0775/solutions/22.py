(n, m, k) = list(map(int, input().split()))
ip = list(map(int, input().split()))
holes = [0 for i in range(n + 1)]
for i in ip:
    holes[i] = 1
pos = 1
b = 0
if holes[1] == 1:
    b = 1
for i in range(k):
    (u, v) = list(map(int, input().split()))
    if u == pos and b == 0:
        pos = v
        if holes[v] == 1:
            b = 1
    elif v == pos and b == 0:
        pos = u
        if holes[u] == 1:
            b = 1
print(pos)

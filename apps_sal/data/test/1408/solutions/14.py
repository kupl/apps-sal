3

n = int(input())
t = []
w = []
n1, n2 = 0, 0
for i in range(n):
    x, y = list(map(int, input().split()))
    t.append(x)
    w.append(y)
    n1 += x == 1
    n2 += x == 2

w1 = []
w2 = []
for i in range(n):
    if t[i] == 1:
        w1.append(w[i])
    else:
        w2.append(w[i])
w1.sort(reverse=True)
w2.sort(reverse=True)

ans = 201
for i in range(201):
    for j in range(min(i // 2, n2) + 1):
        k = min(n1, i - 2 * j)
        thickness = 2 * j + k
        if thickness >= sum(w1[k:]) + sum(w2[j:]):
            ans = min(ans, thickness)

print(ans)


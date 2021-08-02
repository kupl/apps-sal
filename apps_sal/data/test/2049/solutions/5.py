n, m = list(map(int, input().split()))
l = list(map(int, input().split()))
l1 = [0] * (n)
l3 = [0] * n
f = False
v = 0
for i in range(1, n):
    if l[i] < l[i - 1]:
        f = True
        v = i
    if l[i] > l[i - 1] and f:
        f = False
        for j in range(i - 1, v - 1, -1):
            l3[j] = j
        l1[v] = 1
        v = -1

l2 = [0] * (n)
for i in range(1, n):
    l2[i] = l1[i] + l2[i - 1]
s = []
for i in range(m):
    a, b = list(map(int, input().split()))
    t = l2[b - 1] - l2[a - 1]

    if l3[b - 1] >= b - 1:
        t -= 1

    if t > 0:
        s.append("No")
    else:
        s.append("Yes")
print("\n".join(s))

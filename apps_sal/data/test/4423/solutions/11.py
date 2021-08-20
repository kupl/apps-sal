n = int(input())
d = []
ans = [0] * n
for i in range(n):
    (s, p) = input().split()
    p = -int(p)
    d.append([i + 1, s, p])
d2 = sorted(d, key=lambda x: (x[1], x[2]))
for i in range(n):
    print(d2[i][0])

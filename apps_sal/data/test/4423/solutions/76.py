N = int(input())
l = []
for i in range(N):
    (s, p) = input().split()
    l.append([s, int(p), i + 1])
l = sorted(l, key=lambda x: (x[0], -x[1]))
for i in range(N):
    print(l[i][2])

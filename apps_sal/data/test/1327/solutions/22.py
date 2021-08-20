import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
Cake = []
for _ in range(n):
    c = list(map(int, input().split()))
    Cake.append(c)
total = []
for i in range(8):
    total_i = []
    for k in Cake:
        hyouka = 0
        for j in range(3):
            if i >> j & 1:
                hyouka += k[j]
            else:
                hyouka -= k[j]
        total_i.append(hyouka)
    total_i.sort(reverse=True)
    goukei = 0
    for l in range(m):
        goukei += total_i[l]
    total.append(goukei)
print(max(total))

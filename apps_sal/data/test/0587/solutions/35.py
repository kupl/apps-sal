n, k = map(int, input().split())
td = []
for _ in range(n):
    td.append(list(map(int, input().split())))
td.sort(key=lambda x: x[1], reverse=True)
NEW = [1] * (n + 1)
x = 0
y = 0
TOP = []
SUB = []
A = []
for tdi in td[:k]:
    if NEW[tdi[0]] == 1:
        NEW[tdi[0]] = 0
        TOP.append(tdi[1])
        y += 1
    else:
        A.append(tdi[1])
    x += tdi[1]

for tdi in td[k:]:
    if NEW[tdi[0]] == 1:
        SUB.append(tdi[1])
        NEW[tdi[0]] = 0
ans = x + y**2
for i in range(min(k - 1, len(A), len(SUB))):
    x -= A.pop()
    x += SUB[i]
    y += 1
    ans = max(ans, x + y**2)
print(ans)

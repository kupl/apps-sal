n = int(input())
v = list(map(int, input().split()))
vaz = [0 for x in range(n + 10)]
vaz1 = [0 for x in range(n + 10)]
for x in v:
    vaz[x] += 1
ans1 = 0
pz = 1
while pz <= n:
    if vaz[pz] == 0:
        pz += 1
        continue
    ans1 += 1
    pz += 3
for i in range(1, n + 1):
    if vaz[i] == 0:
        continue
    a = vaz[i]
    if vaz1[i - 1] == 0 and a > 0:
        a -= 1
        vaz1[i - 1] = 1
    if vaz1[i] == 0 and a > 0:
        a -= 1
        vaz1[i] = 1
    if vaz1[i + 1] == 0 and a > 0:
        a -= 1
        vaz1[i + 1] = 1
ans2 = 0
for i in range(0, n + 2):
    if vaz1[i] == 1:
        ans2 += 1
print(str(ans1) + " " + str(ans2))

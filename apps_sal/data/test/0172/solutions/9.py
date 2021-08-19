n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
q = [0] * 6
for i in a:
    q[i] += 1
for i in b:
    q[i] += 1
f = True
for i in q:
    if i % 2 != 0:
        f = False
if not f:
    print(-1)
else:
    for i in range(6):
        q[i] //= 2
    aa = [0] * 6
    bb = [0] * 6
    for i in a:
        aa[i] += 1
    for i in b:
        bb[i] += 1
    ans = 0
    for i in range(6):
        ans += abs(q[i] - aa[i])
    print(ans // 2)

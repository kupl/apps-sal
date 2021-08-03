n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
hs1 = [0 for _ in range(a[-1])]
for i in range(n):
    hs1[a[i] - 1] += 1
pluser = 0
hs = [0 for _ in range(a[-1])]
for i in range(a[-1]):
    pluser += hs1[a[-1] - i - 1]
    hs[a[-1] - i - 1] = pluser
floor = a[-1] - 1
ans = 0
count = 0
while floor > a[0] - 1:
    while floor > a[0] - 1 and count + hs[floor] <= k:
        count += hs[floor]
        floor -= 1
    ans += 1
    count = 0
print(ans)

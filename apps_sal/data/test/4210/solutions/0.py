inp = input().split()
n = int(inp[0])
k = int(inp[1])

a = input().split()
for i in range(n):
    a[i] = int(a[i])


bank = {}

for i in range(n):
    arg = (len(str(a[i])), a[i] % k)
    bank[arg] = bank.get(arg, 0) + 1

ans = 0
for i in range(n):
    ten = 1
    for j in range(1, 11):
        ten *= 10
        frontMod = (a[i] * ten) % k
        req = (k - frontMod) % k

        got = bank.get((j, req), 0)
        ans += got

for i in range(n):
    cur = str(a[i])
    cur = cur * 2
    tst = int(cur)
    if(tst % k == 0):
        ans -= 1

print(ans)

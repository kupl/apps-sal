h, w = [int(x) for x in input().split()]
n = int(input())
a = [int(x) for x in input().split()]

ans = [["0"] * w for x in range(h)]

now = 0
for i in range(n):
    for j in range(a[i]):
        cc = now
        x = cc // w
        cc %= w
        if x % 2 == 0:
            y = cc
        else:
            y = w - cc - 1
        ans[x][y] = str(i + 1)
        now += 1

for i in range(h):
    print(" ".join(ans[i]))

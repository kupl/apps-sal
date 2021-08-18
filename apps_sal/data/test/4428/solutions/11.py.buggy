n = int(input())
a = list(map(int, input().split()))

x = 0
y = 0
z = sum(a)
pos = -1

for i in range(n):
    x += a[i]
    z -= a[i]
    if x >= z:
        pos = i
        break

l, r = pos, pos + 1

while True:
    # print(l, r)
    if x > z and l >= 0:
        x -= a[l]
        l -= 1
    elif x < z and r < n:
        z -= a[r]
        r += 1
    elif x == z:
        print(x)
        return
    elif l < 0 or r >= n:
        print(0)
        return

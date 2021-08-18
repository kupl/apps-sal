n, x = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * (100001)
c = [0] * 100001
for i in a:
    b[i] += 1
    if b[i] >= 2:
        print(0)
        return
for i in a:
    b[i] -= 1
    if b[i & x] >= 1:
        print(1)
        return
    b[i] += 1
for i in a:
    c[i & x] += 1
    if c[i & x] >= 2:
        print(2)
        return
print(-1)

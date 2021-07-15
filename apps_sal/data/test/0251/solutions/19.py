n,k = map(int, input().split())
L = list(map(int, input().split()))
ma = max(L)
f = [0]*(ma+1)
for i in L:
    f[i] += 1
for i in reversed(range(ma)):
    f[i] = f[i] + f[i+1]
c = 0
s = 0
if f[ma] == n:
    print(0)
    quit()
for i in reversed(range(ma+1)):
    if f[i] == n:
        break
    s += f[i]
    if s > k:
        c += 1
        s = f[i]
print(c+1)

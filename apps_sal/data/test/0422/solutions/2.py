n, k = map(int, input().split())
o = [int(t) for t in (input()+' '+input()).split()]
f, s = 0, 0
for i in range(n):
    f = max(0, o[i] + f - k * o[i+n])
    s = max(0, o[i+n] + s - k * o[i])
    if f > k or s > k:
        print('NO')
        return
print('YES')

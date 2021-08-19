from sys import stdin


def nii():
    return map(int, stdin.readline().split())


def lnii():
    return list(map(int, stdin.readline().split()))


(x, y, a, b, c) = nii()
p = sorted(lnii(), reverse=True)
q = sorted(lnii(), reverse=True)
r = sorted(lnii(), reverse=True)
l = p[:x] + q[:y]
l.sort()
ans = 0
for i in range(x + y):
    if i < c:
        ans += max(l[i], r[i])
    else:
        ans += l[i]
print(ans)

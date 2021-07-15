def preobr(s):
    h, m = list(map(int,s.split()))
    return h * 60 + m


n, s = list(map(int,input().split()))
t = preobr(input())
s += 1
fl = False
if t >= s:
    res = 0
    fl = True
for i in range(n - 1):
    new_t = preobr(input())
    if fl:
        continue
    if new_t - t >= 2 * s:
        res = t + s
        fl = True
    else:
        t = new_t
if not fl:
    res = t + s
print(res // 60, res % 60)
        


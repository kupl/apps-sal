string = input()
n = string.count('n')
i = string.count('i')
e = string.count('e')
t = string.count('t')
n -= 1
vn = n / 2
ve = e / 3
vi = i
vt = t
ans = max(0, min(vn, ve, vi, vt))
ans = int(ans)
print(ans)

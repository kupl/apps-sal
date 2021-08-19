(x, k) = map(int, input().split())
p = [1] * 4001
p[0] = p[x] = 0
for i in range(k):
    t = list(map(int, input().split()))
    if t[0] == 1:
        p[t[1]] = p[t[2]] = 0
    else:
        p[t[1]] = 0
s = a = b = 0
for i in p:
    if i:
        s += 1
    elif s:
        a += s
        b += (s + 1) // 2
        s = 0
print(str(b) + ' ' + str(a))

p, k = map(int, input().split())
r = [p % k]
p = p // k
while 1:
    if p <= 0 and -p < k:
        break
    p, q = divmod(-p, k)
    r.append(q)
if p:
    r.append(-p)
print(len(r))
print(*r, sep=' ')

(n, k) = [int(x) for x in input().strip().split(' ', 1)]
a = [int(x) for x in input().strip().split(' ')]
b = [int(x) for x in input().strip().split(' ')]
c = [(xb - xa, xa, xb) for (xa, xb) in zip(a, b)]
c.sort(key=lambda x: x[0], reverse=True)
cnt = sum([cx[1] for cx in c[:k]])
while k < n and c[k][0] >= 0:
    cnt += c[k][1]
    k = k + 1
if k < n:
    cnt += sum((cx[2] for cx in c[k:]))
print(cnt)

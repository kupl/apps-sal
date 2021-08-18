n, k = list(map(int, input().split()))
data = list(map(int, input().split()))
if k > 3 * n:
    print(max(data))
    return
q = data

cnt = 0
c1, c2 = q[0], q[1]
q = q[2:]

while cnt < k:
    if c1 > c2:
        cnt += 1
    else:
        c1, c2 = c2, c1
        cnt = 1
    q.append(c2)
    c2 = q[0]
    q = q[1:]
print(c1)

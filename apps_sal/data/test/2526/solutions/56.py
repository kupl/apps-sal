(x, y, a, b, c) = list(map(int, input().split()))
p = sorted(map(int, input().split()), reverse=True)
q = sorted(map(int, input().split()), reverse=True)
r = sorted(map(int, input().split()))
v = 0
c = sorted(p[0:x] + q[0:y])
for i in range(x + y):
    if len(r):
        if c[i] < r[-1]:
            c[i] = r.pop()
    else:
        break
print(sum(c))

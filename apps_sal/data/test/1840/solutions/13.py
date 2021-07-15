n, m = list(map(int, input().split()))
a = sorted([(int(x), y) for x, y in zip(input().split(), list(range(n)))])
b = []
for _ in range(m):
    b.append(list(map(int, input().split())))
b = sorted(b)
p1 = 0
p2 = 0
s = 0
ans = [0 for _ in range(len(a))]
while p1 < len(a) and p2 < len(b):
    # print(p1, p2)
    if a[p1][0] >= b[p2][0]:
        s += b[p2][1]
        p2 += 1
    else:
        ans[a[p1][1]] = s
        p1 += 1
while p1 < len(a):
    ans[a[p1][1]] = s
    p1 += 1
print(" ".join(list(map(str, ans))))


n, m, x = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]
ans = []
# n冊の本において買うか買わないかの2通りなので2**n
for i in range(2**n):
    # リストの中身は値段1と理解度m個
    a = [0] * (m + 1)
    com = i
    for j in range(n):
        if com >= (2**(n - j - 1)):
            com -= 2**(n - j - 1)
            for k in range(m + 1):
                a[k] += c[j][k]
    price = a[0]
    del a[0]
    if all(a[j] >= x for j in range(m)):
        # print(price)
        ans.append(price)
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))

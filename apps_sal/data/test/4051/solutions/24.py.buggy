n = int(input())
a = list(map(int, input().split()))
b = sorted(a, reverse=True)
c = []
for i in range(n):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1] + 1 or a[j] < a[j + 1] - 1:
            print('NO')
            return
    c += [max(a)]
    a.remove(max(a))
assert b == c, (b, c)
print('YES')

def get_ints():
    return list(map(int, input().split()))


n = int(input())
a, b = [], []
for i in range(n):
    x, y = get_ints()
    a.append(x - y)
    b.append(x + y)

a.sort()
b.sort()
ans = max(a[-1] - a[0], b[-1] - b[0])
print(ans)

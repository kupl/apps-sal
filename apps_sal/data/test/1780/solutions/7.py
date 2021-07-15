n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a_min = min(a.count(1), a.count(-1))
s = ''
for i in range(m):
    l, r = list(map(int, input().split()))
    length = r - l + 1
    s += '0\n' if length % 2 or length // 2 > a_min else '1\n'
print(s)


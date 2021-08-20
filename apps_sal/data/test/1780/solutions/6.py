(n, m) = map(int, input().split())
a = list(map(int, input().split()))
a_plus = a.count(1)
a_minus = a.count(-1)
s = ''
for i in range(m):
    (l, r) = map(int, input().split())
    length = r - l + 1
    s += '0\n' if length % 2 or length // 2 > a_plus or length // 2 > a_minus else '1\n'
print(s)

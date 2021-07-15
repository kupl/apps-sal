n, m = map(int, input().split())
a_plus = input().split().count('1')
a_min = min(a_plus, n - a_plus) * 2
res = []
for i in range(m):
    l, r = map(int, input().split())
    length = r - l + 1
    res += ['0'] if length % 2 or length > a_min else ['1']
print('\n'.join(res))

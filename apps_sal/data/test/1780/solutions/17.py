n, m = map(int, input().split())
a_plus = input().split().count('1')
a_min = min(a_plus, n - a_plus) * 2
res = ['1'] * m
for i in range(m):
    l, r = map(int, input().split())
    length = r - l + 1
    if length > a_min or length % 2:
        res[i] = '0'
print('\n'.join(res))

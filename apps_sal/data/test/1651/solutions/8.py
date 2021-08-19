(s, p) = map(int, input().split())
delta = s ** 2 - 4 * p
m = (s + delta ** 0.5) / 2
n = (s - delta ** 0.5) / 2
if m + n == s and m * n == p:
    print('Yes')
else:
    print('No')

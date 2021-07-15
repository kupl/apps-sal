3

Na, Nb = map(int, input().split())
k, m = map(int, input().split())

assert 1 <= k <= Na
assert 1 <= m <= Nb

a = list(map(int, input().split()))
b = list(map(int, input().split()))

assert len(a) == Na
assert len(b) == Nb

print('YES' if a[k-1] < b[-m] else 'NO')

(n, m) = list(map(int, input().split()))
a = input().split().count('1')
b = min(a, n - a) * 2
ans = []
for i in range(m):
    (l, r) = list(map(int, input().split()))
    length = r - l + 1
    ans += ['0'] if length % 2 or length > b else ['1']
print('\n'.join(ans))

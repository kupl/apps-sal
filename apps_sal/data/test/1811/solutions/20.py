cnt = lambda s, i: s.count(i)
ii = lambda: int(input())
si = lambda: input()
f = lambda: map(int, input().split())
il = lambda: list(map(int, input().split()))
n, k = f()
s = list(si().split('.'))
s.pop(0)
s.pop(-1)
for i in s:
    if len(i) >= k:
        print('NO'); return
print('YES')

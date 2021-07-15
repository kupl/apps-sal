__author__ = 'asmn'
n, m = tuple(map(int, input().split()))
a = list(map(int, input().split()))

s = set()
ans = [0] * n
for i in reversed(range(n)):
    s.add(a[i])
    ans[i] = len(s)

for i in range(m):
    print(ans[int(input()) - 1])

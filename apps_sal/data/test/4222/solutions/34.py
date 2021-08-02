import itertools
n, k = map(int, input().split())
ans = 0
l = []
for i in range(k):
    d = int(input())
    l.append(input().split())

l = list(itertools.chain.from_iterable(l))
l = [int(i) for i in l]

for i in range(1, n + 1):
    if not i in l:
        ans += 1
print(ans)

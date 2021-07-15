import collections
N = int(input())
s = ["".join(sorted(input())) for i in range(N)]

ans = 0
cnt = collections.Counter(s)
for i in cnt.values():
    if i > 1:
        ans += i*(i-1)//2

print(ans)

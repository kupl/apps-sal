import collections
N = int(input())
s = ["".join(sorted(input())) for _ in range(N)]
s.sort()
C = collections.Counter(s)
D = C.most_common()

ans = 0
for i in D:
    ans += i[1] * (i[1] - 1) // 2
print(ans)

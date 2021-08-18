import collections
N = int(input())
A = list(map(int, input().split()))
c = collections.Counter(A)
most = c.most_common()
ans = len(most)
eaten = 0
for t in most:
    if t[1] != 1:
        eaten += t[1] - 1
if eaten % 2 == 1:
    print(ans - 1)
else:
    print(ans)

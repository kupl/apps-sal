from collections import Counter
N = int(input())
A = [int(input()) for _ in range(N)]
cnt = dict(Counter(A))
ans = []
for k, v in list(cnt.items()):
    if v % 2 != 0:
        ans.append(k)
print((len(ans)))


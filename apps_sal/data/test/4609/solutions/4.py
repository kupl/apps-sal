from collections import Counter
N = int(input())
A = [int(input()) for i in range(N)]

cnt = Counter(A)
ans = 0
for k, v in cnt.items():
    if v % 2 == 1:
        ans += 1

print(ans)

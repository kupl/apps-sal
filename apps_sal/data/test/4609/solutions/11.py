from collections import Counter

n = int(input())
A = [int(input()) for _ in range(n)]
cnt_A = Counter(A)

ans = 0
for v in cnt_A.values():
    if v % 2 == 1:
        ans += 1
print(ans)

import sys
import itertools

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
lst = [a, b, c, d, e]
ans = 1 << 10
for i in itertools.permutations(lst, 5):
    cnt = 0
    for num, j in enumerate(i):
        if num == 4:
            cnt += j
            break
        if j % 10 != 0:
            cnt += 10 * (j // 10) + 10
        else: cnt += j
    ans = min(ans, cnt)

print(ans)

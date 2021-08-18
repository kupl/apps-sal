from itertools import combinations
n = int(input())
s = sorted([int(input()) for _ in range(n)])

ans = sum(s)
if ans % 10 != 0:
    print(ans)
elif all(i % 10 == 0 for i in s):
    print(0)
else:
    for i in range(1, n):
        for j in combinations(s, i):
            t = sum(j)
            if (ans - t) % 10 != 0:
                print(ans - t)
                return

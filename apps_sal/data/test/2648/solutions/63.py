from collections import Counter
n = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)
ans = len(cnt)
if ans % 2 == 0:
    print(ans - 1)
else:
    print(ans)

from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = list(Counter(a).values())
c.sort()
ans = n
cnt = 0
for i in range(n):
    m = i + 1 - cnt
    while c and c[-1] > ans // m:
        ans -= c.pop()
        cnt += 1
        m -= 1
    print(ans // m)

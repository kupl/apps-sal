__author__ = 'cmashinho'
(n, m) = map(int, input().split())
ans = 0
for _ in range(n):
    l = list(map(int, input().split()))
    for i in range(1, len(l), 2):
        if l[i] == 1 or l[i - 1] == 1:
            ans += 1
print(ans)

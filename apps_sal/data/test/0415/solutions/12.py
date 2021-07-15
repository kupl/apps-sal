'''input
5
100 200 1 1 1
5
1 2 3 4 5
2
101 99

'''
n = int(input())
a = [0] + [int(x) - 100 for x in input().split()]
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + a[i + 1]
ans = 0
q = [0]
for i in range(1, n + 1):
    x = -1
    y = len(q)
    while y - x > 1:
        m = (x + y) >> 1
        if s[q[m]] < s[i]:
            y = m
        else:
            x = m
    if y < len(q):
        ans = max(ans, i - q[y])
    if s[i] < s[q[-1]]:
        q += [i]
print(ans)


n, m = map(int, input().split())
*s, = map(int, input()[::-1])
i = 0
a = []
while i < n:
    j = min(n, i + m)
    while s[j]: j -= 1
    if j == i:
        print(-1)
        return
    a += j - i,
    i = j
print(*a[::-1])

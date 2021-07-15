n, t, c = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
l = 0
i = 0
while i < len(a):
    while i < len(a) and a[i] <= t:
        i += 1
    L = i - l
    if L >= c:
        cnt += (L - c + 1)
    i += 1
    l = i
print(cnt)

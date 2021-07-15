n = int(input())
a = list(map(int, input().split()))
ret, s = 0, sum(a)

if s % 3 == 0:
    p1 = s // 3
    p2 = s - p1
    s = c = 0
    for i in range(n - 1):
        s += a[i]
        if s == p2:
            ret += c
        if s == p1:
            c += 1
print(ret)


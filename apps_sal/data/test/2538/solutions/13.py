n = int(input())
for i in range(n):
    (s, i, e) = (int(i) for i in input().split())
    if s > i + e:
        print(e + 1)
    elif s + e <= i:
        print(0)
    else:
        r = s - i
        r = e + r
        t = 0
        if r % 2:
            t = 1
        r = r // 2
        if t:
            r += 1
        print(r)

n = int(input())
a = list(map(int, input().split()))
(cnt, t) = (0, 0)
for x in a:
    if x > 3:
        t += 1
    else:
        t = 0
    cnt += t // 3
    t %= 3
print(cnt)

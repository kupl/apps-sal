n, x, y = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
if x > y:
    print(n)
else:
    for i in a:
        if i <= x:
            cnt += 1
    print(cnt // 2 + cnt % 2)

n = int(input())
a = list(map(int, input().split()))
cnt = 0
d = 0
for i in a:
    if i in {4, 5}:
        d += 1
        if d == 3:
            cnt += 1
            d = 0
    else:
        d = 0
print(cnt)

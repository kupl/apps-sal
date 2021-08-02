n = int(input())
a = list(map(int, input().split()))

i = 0
cnt = 0
ok = True
while i < n:
    if a[i] == 0:
        if cnt % 2 == 1:
            ok = False
            break
        else:
            cnt = 0
    else:
        cnt += a[i]
    i += 1

if not ok or cnt % 2 == 1:
    print("NO")
else:
    print("YES")

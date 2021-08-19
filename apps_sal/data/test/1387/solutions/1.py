(n, t) = map(int, input().split())
arr = list(map(int, input().split()))
cur = 0
was = False
while cur < n:
    try:
        cur = cur + arr[cur]
        if cur == t - 1:
            was = True
    except:
        break
if was:
    print('YES')
else:
    print('NO')

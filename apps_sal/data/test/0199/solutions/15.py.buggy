n, s = map(int, input().split())
k = list(map(int, input().split()))
sumk = sum(k)
mink = min(k)
if sumk < s:
    print(-1)
    return
if sumk - n * mink >= s:
    print(mink)
else:
    s -= sumk - n * mink
    if s % n == 0:
        print(mink - s // n)
    else:
        print(mink - s // n - 1)

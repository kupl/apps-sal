n = int(input())
a = list(map(int, input().split()))
l = 0
for i in a:
    if i == 0:
        l += 1
r = n - l
cnt = 0
for i in a:
    cnt += 1
    if i == 0:
        l -= 1
    else:
        r -= 1
    if (l == 0) or (r == 0):
        print(cnt)
        return


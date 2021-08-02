n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in a:
    if i >= sum(a) / (4 * m):
        cnt += 1
if cnt >= m:
    print("Yes")
else:
    print("No")

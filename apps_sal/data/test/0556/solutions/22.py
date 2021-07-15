l, r, k = map(int, input().split())
cur = 1
flag = True
while cur <= r:
    if cur >= l and cur <= r:
        print(cur, end=" ")
        flag = False
    cur *= k
if flag:
    print(-1)

def read(): return map(int, input().split())


l, r, k = read()
cur = 1
flag = 0
while cur <= r:
    if cur >= l:
        flag = 1
        print(cur, end=' ')
    cur *= k
if flag == 0:
    print(-1)

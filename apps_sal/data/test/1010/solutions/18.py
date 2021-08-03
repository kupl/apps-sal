n = int(input())
lst = list(map(int, input().split()))
ans = 1
cnt = 0
if 1 in lst:
    p = lst.index(1)
    for i in range(p, n):
        if lst[i] == 1:
            if cnt != 0:
                ans *= cnt
                cnt = 0
        cnt += 1
    print(ans)
else:
    print(0)

n = int(input())
a = list(map(int, input().split()))
used = [False] * n
flag = True
cur = 0
ans = 0
i = 0
while cur < n:
    ans += 1
    if (i == 0):
        for i in range(n):
            if (not used[i]) and (a[i] <= cur):
                cur += 1
                used[i] = True
    else:
        for i in range(n - 1, -1, -1):
            if (not used[i]) and (a[i] <= cur):
                cur += 1
                used[i] = True
print(ans - 1)
    


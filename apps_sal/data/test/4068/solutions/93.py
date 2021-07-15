n, m = list(map(int,input().split()))
lst = [-1 for i in range(n + 1)]
for i in range(m):
    x = int(input())
    lst[x] = 0

lst[0] = 1
for i in range(1, n + 1):
    if (i == 1):
        if(lst[1] == -1):
            lst[1] = 1
    elif (lst[i] == 0):
        pass
    else:
        lst[i] = (lst[i - 1] + lst[i - 2])%(1000000007)

print((lst[n]))


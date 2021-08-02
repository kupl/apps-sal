n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(n):
    if(i == 0):
        pass
    elif (i == n - 1):
        pass
    else:
        a = p[i - 1]
        b = p[i]
        c = p[i + 1]
        lst = [a, b, c]
        lst.sort()
        if (lst[1] == b):
            ans = ans + 1
print(ans)

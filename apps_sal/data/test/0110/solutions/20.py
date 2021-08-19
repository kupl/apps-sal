n = int(input())
l = list(map(int, input().split()))
ans = [0] * n
neg = 0
for i in l:
    if i < 0:
        neg += 1
if neg % 2 == 0:
    if n % 2 == 0:
        for i in range(n):
            if l[i] < 0:
                ans[i] = l[i]
            else:
                ans[i] = -1 - l[i]
        for i in ans:
            print(i, end=' ')
    else:
        for i in range(n):
            if l[i] < 0:
                ans[i] = l[i]
            else:
                ans[i] = -1 - l[i]
        f = ans.index(min(ans))
        ans[f] = -ans[f] - 1
        for i in ans:
            print(i, end=' ')
elif n % 2 == 0:
    for i in range(n):
        if l[i] < 0:
            ans[i] = l[i]
        else:
            ans[i] = -1 - l[i]
    for i in ans:
        print(i, end=' ')
else:
    for i in range(n):
        if l[i] < 0:
            ans[i] = l[i]
        else:
            ans[i] = -1 - l[i]
    f = ans.index(min(ans))
    ans[f] = -ans[f] - 1
    for i in ans:
        print(i, end=' ')

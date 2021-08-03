q = int(input())
ans = []
for i in range(q):
    n = int(input())
    if n % 4 == 0:
        ans.append(n // 4)
    elif n % 4 == 2:
        if n >= 6:
            ans.append(n // 4)
        else:
            ans.append(-1)
    elif n % 4 == 1:
        if n >= 9:
            ans.append(n // 4 - 1)
        else:
            ans.append(-1)
    else:
        if n >= 15:
            ans.append(n // 4 - 1)
        else:
            ans.append(-1)
for i in ans:
    print(i)

m, k = list(map(int, input().split()))
if m == 1:
    if k == 0:
        print((0, 0, 1, 1))
    else:
        print((-1))
else:
    s = 2 ** m
    if k >= s:
        print((-1))
    else:
        ans = [k]
        for i in range(s):
            if i != k:
                ans.append(i)
        ans.append(k)
        for i in range(s - 1, -1, -1):
            if i != k:
                ans.append(i)
        print((*ans))

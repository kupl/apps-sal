N = int(input())
a = list(map(int, input().split()))
m = min(a)
M = max(a)


flag = 1
plus = 0
minus = 0
for x in a:
    if x > 0:
        plus += 1
    elif x < 0:
        minus += 1
if m*M < 0:
    if m + M >= 0:
        id = a.index(M)
        print((minus + N-1))
        for i in range(N):
            if a[i] < 0:
                a[i] += M
                print((id+1, i+1))

    else:
        id = a.index(m)
        print((plus + N-1))
        for i in range(N):
            if a[i] > 0:
                a[i] += m
                print((id+1, i+1))

        flag = 0

else:
    print((N-1))
    if m < 0:
        flag = False


if flag:  # 正の数列
    # M = max(a)
    # id = a.index(M)
    for i in range(1, N):
        # if i == 0:
        #     a[i] += M
        #     print(id+1, 1)
        # else:
        a[i] += a[i-1]
        print((i, i+1))

else:
    # m = min(a)
    # id = a.index(m)
    for i in range(N-2, -1, -1):
        # if i == N-1:
        #     a[i] += m
        #     print(id, i+1)
        # else:
        a[i] += a[i+1]
        print((i+2, i+1))
# print(a)


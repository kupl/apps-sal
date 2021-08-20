t = int(input())
for you in range(t):
    l = input().split()
    n = int(l[0])
    k = int(l[1])
    l = input().split()
    li = [int(i) for i in l]
    if k == 1:
        poss = 1
        for i in li:
            if i != li[0]:
                poss = 0
                break
        if poss:
            print(1)
        else:
            print(-1)
        continue
    count = 0
    for i in range(n - 1):
        if li[i] != li[i + 1]:
            count += 1
    count += 1
    for i in range(1, 400):
        if (i - 1) * (k - 1) + k >= count:
            ans = i
            break
    print(ans)

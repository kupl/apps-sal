q = int(input())
for i in range(q):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = [0] * n
    for i in range(n):
        if ans[i] == 0:
            numbers_now = []
            now = a[a[i] - 1]
            numbers_now.append(i)
            numbers_now.append(a[i] - 1)
            count = 1
            while now != a[i]:
                now = a[now - 1]
                numbers_now.append(now - 1)
                count += 1
            for i in numbers_now:
                ans[i] = count
        else:
            continue
    print(*ans)

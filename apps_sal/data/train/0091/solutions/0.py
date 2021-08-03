t = int(input())
for faw in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    nun = []
    ans = []
    f = True
    for i in range(1, n + 1):
        if a[i] == a[i - 1]:
            if len(nun) == 0:
                f = False
                break
            else:
                ans.append(nun.pop())
        else:
            ans.append(a[i])
            for i in range(a[i - 1] + 1, a[i]):
                nun.append(i)
    if f:
        print(*ans)
    else:
        print(-1)

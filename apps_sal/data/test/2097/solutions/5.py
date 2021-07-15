N = int(input())
for _ in range(N):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            ans += 1
            lst[i] += 1

    if sum(lst) == 0:
        ans += 1
    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 0:
        cnt = dict()
        for i in a:
            if not i in cnt:
                cnt[i] = 1
            else:
                cnt[i] += 1
        ans = "Second"
        for i in cnt:
            if cnt[i] % 2 == 1:
                ans = "First"
                break
    else:
        ans = "Second"
    print(ans)

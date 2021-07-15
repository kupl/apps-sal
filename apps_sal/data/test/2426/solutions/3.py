t = int(input().strip())
for _ in range(t):
    #a,b = map(int,input().strip().split())
    n = int(input().strip())
    nums = [int(i) for i in input().strip().split()]
    if n == 1 and nums[0] % 2 != 0:
        print(-1)
    else:
        has = False
        for i in range(n):
            if nums[i] % 2 == 0:
                ans = i
                has = True
                break
        if has:
            print(1)
            print(ans + 1)
        else:
            print(2)
            print(1,2)


t = int(input().strip())
for i in range(t):
    n, k = list(map(int, input().strip().split()))
    nums = [int(i) for i in input().strip().split()]
    cur_k = 0
    ans = []
    has = True
    if k == 1:
        if sum(nums) % 2 == 0:
            print("NO")
        else:
            print("YES")
            print(n)
    else:
        for i in range(n):
            if cur_k == k - 1:
                if ans[-1] != n:
                    if sum(nums[ans[-1]:]) % 2 == 0:
                        has = False
                        break
                    else:
                        cur_k += 1
                        ans.append(n)
                        break
            if nums[i] % 2 == 1:
                ans.append(i + 1)
                cur_k += 1
        #print("ans ", ans)
        if cur_k < k or not has:
            print("NO")
        else:
            print("YES")
            print(' '.join(str(i) for i in ans))

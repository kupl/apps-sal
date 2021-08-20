for i in range(int(input())):
    n = int(input())
    w = set()
    [w.add(int(j)) for j in input().split()]
    data = list(w)
    data.sort()
    nums = [data[-1]]
    ind = len(data) - 2
    cnt = 1
    while ind >= 0:
        if cnt == 1:
            if nums[0] % data[ind] != 0:
                nums.append(data[ind])
                cnt += 1
        elif nums[0] % data[ind] != 0 and nums[1] % data[ind] != 0:
            nums.append(data[ind])
            break
        ind -= 1
    ans = sum(nums)
    if len(data) >= 2:
        nums2 = [data[-2]]
        ind = len(data) - 3
        cnt = 1
        while ind >= 0:
            if cnt == 1:
                if nums2[0] % data[ind] != 0:
                    nums2.append(data[ind])
                    cnt += 1
            elif nums2[0] % data[ind] != 0 and nums2[1] % data[ind] != 0:
                nums2.append(data[ind])
                break
            ind -= 1
        ans = max(ans, sum(nums2))
    print(ans)

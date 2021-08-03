def main():

    n = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    flg = True
    while flg:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                num = nums[i] / 2
                nums[i] = num
            else:
                flg = False
                break
        if flg:
            ans += 1

    print(ans)


def __starting_point():
    main()


__starting_point()

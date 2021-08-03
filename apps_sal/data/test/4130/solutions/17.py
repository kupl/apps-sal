def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    nums = set()
    for i in arr:
        if i - 1 > 0 and ((i - 1) not in nums):
            nums.add(i - 1)
        elif i not in nums:
            nums.add(i)
        elif (i + 1) not in nums:
            nums.add(i + 1)

    print(len(nums))


main()

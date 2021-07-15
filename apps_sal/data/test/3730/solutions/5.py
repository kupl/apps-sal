ints = int(input())
nums = list(map(int, input().split(' ')))

if ints == 1:
    print(1)
elif ints == 2:
    print(2)
else:        
    left = [1]*ints
    right = [1]*ints

    #how many you can extend to the left
    #[1, 1, 2, 1, 2, 3]
    #the 3 can go to [1, 2, 3]
    #both 2s can go to [1, 2]
    for i in range(ints-1):
        if nums[i+1] > nums[i]:
            left[i+1] += left[i]

    #how many you can extend to the right
    #the 2nd 1 can go to [1, 2]
    #the 3rd 1 can go to [1, 2, 3]
    nums.reverse()
    for i in range(ints-1):
        if nums[i+1] < nums[i]:
            right[i+1] += right[i]

    nums.reverse()
    right.reverse()

    maximum = 2
    for i in range(1, ints-1):
        if nums[i-1]+1 < nums[i+1]:
            maximum = max(maximum, left[i-1] + right[i+1] + 1)
        else:
            maximum = max(maximum, max(left[i-1]+1, right[i+1]+1))

    maximum=max(maximum, left[ints-2]+1, right[1]+1)
    print(maximum)


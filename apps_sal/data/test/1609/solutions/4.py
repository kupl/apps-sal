n = int(input())

nums = [False] * n
seen = [False] * n
i = 0
A = list(map(int, input().split()))

# First walk
for num in A:
    if 1 <= num <= n:
        nums[num - 1] = True

# Second walk
for num in A:
    if 1 <= num <= n:
        if not seen[num - 1]:
            seen[num - 1] = True
            print(num, end = " ")
        else:
            while nums[i]:
                i += 1
            nums[i] = True
            i += 1
            print(i, end = " ")
    else:
        while nums[i]:
            i += 1
        nums[i] = True
        i += 1
        print(i, end = " ")

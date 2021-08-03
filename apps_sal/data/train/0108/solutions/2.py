t = int(input().rstrip())

for i in range(t):
    n = int(input().rstrip())
    nums = list(map(int, input().rstrip().split()))
    forw = 0
    back = n - 1

    for j in range(n):
        if nums[j] >= j:
            forw = j
        else:
            break

    for j in range(1, n + 1):
        if nums[-j] >= j - 1:
            back = n - j
        else:
            break

    if forw >= back:
        print("Yes")
    else:
        print("No")

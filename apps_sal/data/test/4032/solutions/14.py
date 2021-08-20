(n, k) = map(int, input().split())
difficulties = list(map(int, input().split()))
solved = True
count = 0
left = 0
right = n - 1
while solved and left <= right:
    solved = False
    if difficulties[left] <= k:
        left += 1
        solved = True
        count += 1
    elif difficulties[right] <= k:
        right -= 1
        solved = True
        count += 1
print(count)

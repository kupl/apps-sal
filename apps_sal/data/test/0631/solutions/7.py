for t in range(int(input())):
    n, m = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    if sum(nums) == m:
        print("YES")
    else:
        print("NO")
